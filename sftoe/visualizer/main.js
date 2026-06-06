/* ============================================================
   SFTOE Universe Visualizer — Main Application
   ============================================================ */

(function () {
  'use strict';

  // ─── Configuration ────────────────────────────────────────
  const WS_URL = 'ws://localhost:8765';
  const TRAIL_LENGTH = 40;
  const STAR_COUNT = 6000;
  const RECONNECT_DELAY_MS = 3000;
  const MAX_EVENTS = 5;
  const BASE_PARTICLE_SIZE = 0.25;

  // ─── Color Palettes ──────────────────────────────────────
  const PARTICLE_COLORS = {
    // Leptons — warm
    electron: 0xdc143c, // crimson
    muon:     0xffbf00, // amber
    tau:      0xffd700, // gold
    lepton:   0xdc143c, // fallback

    // Quarks — cool
    up:       0x2563eb, // sapphire
    down:     0x14b8a6, // teal
    strange:  0x8b5cf6, // violet
    charm:    0x06b6d4, // cyan
    bottom:   0x1e40af, // deep blue
    top:      0x0ea5e9, // sky
    quark:    0x2563eb, // fallback

    // Bosons — ethereal
    photon:   0xfef08a,
    gluon:    0x86efac,
    w_boson:  0xc4b5fd,
    z_boson:  0xa5b4fc,
    higgs:    0xfbbf24,
    boson:    0xc4b5fd, // fallback
  };

  const FORCE_COLORS = {
    gravity: 0x3b82f6,
    em:      0xfbbf24,
    strong:  0x22d3ee,
    weak:    0x8b5cf6,
  };

  // Quark color-charge hues (r / g / b mapped to actual RGB for aura)
  const COLOR_CHARGE_HUES = {
    1: 0xff3333, // red
    2: 0x33ff33, // green
    3: 0x3333ff, // blue
  };

  // ─── State ────────────────────────────────────────────────
  let scene, camera, renderer, orbitControls;
  let clock = new THREE.Clock();
  let ws = null;

  // Simulation state
  let playing = true;
  let speedMultiplier = 1;
  let currentTick = 0;
  let latestFrame = null;
  let pendingStep = false;

  // Particle tracking
  const particleMeshes = new Map();    // name → { group, sphere, glow, light, label }
  const particleTrails = new Map();    // name → { positions:[], line }
  const couplingLines  = [];
  let focusedParticle  = null;

  // Camera modes
  let cameraMode = 'orbit'; // 'orbit' | 'fly'
  const flyState = { forward: 0, right: 0, up: 0, yaw: 0, pitch: 0 };
  const keysDown = new Set();
  let mouseCapture = false;

  // Raycaster for picking
  const raycaster = new THREE.Raycaster();
  const mouseNDC  = new THREE.Vector2();

  // ─── DOM References ───────────────────────────────────────
  const DOM = {};
  function cacheDom() {
    DOM.container      = document.getElementById('canvas-container');
    DOM.connStatus     = document.getElementById('connection-status');
    DOM.connText       = document.getElementById('connection-text');
    DOM.hudTick        = document.getElementById('hud-tick');
    DOM.hudSpeed       = document.getElementById('hud-speed');
    DOM.hudCount       = document.getElementById('hud-particle-count');
    DOM.hudEnergy      = document.getElementById('hud-energy');
    DOM.hudInvariants  = document.getElementById('hud-invariants');
    DOM.hudEvents      = document.getElementById('hud-events');
    DOM.btnPlay        = document.getElementById('btn-play');
    DOM.btnStep        = document.getElementById('btn-step');
    DOM.speedSlider    = document.getElementById('speed-slider');
    DOM.speedDisplay   = document.getElementById('speed-display');
    DOM.tickCounter    = document.getElementById('tick-counter');
    DOM.cameraModeText = document.getElementById('camera-mode-text');
    DOM.particleInfo   = document.getElementById('particle-info');
    DOM.infoClose      = document.getElementById('info-close');
    DOM.infoName       = document.getElementById('info-name');
    DOM.infoType       = document.getElementById('info-type');
    DOM.infoState      = document.getElementById('info-state');
    DOM.infoMass       = document.getElementById('info-mass');
    DOM.infoGen        = document.getElementById('info-gen');
    DOM.infoPos        = document.getElementById('info-pos');
    DOM.infoVel        = document.getElementById('info-vel');
    DOM.infoColor      = document.getElementById('info-color');
  }

  // ─── Helpers ──────────────────────────────────────────────
  function lerp(a, b, t) { return a + (b - a) * t; }
  function clamp(v, lo, hi) { return Math.max(lo, Math.min(hi, v)); }

  function formatSpeed(s) {
    if (s >= 1000) return (s / 1000).toFixed(s >= 10000 ? 0 : 1) + 'k×';
    if (s >= 100) return Math.round(s) + '×';
    if (s >= 10)  return s.toFixed(1) + '×';
    return s.toFixed(2) + '×';
  }

  function resolveColor(particle) {
    // Try specific name-based color first
    const baseName = particle.name.replace(/_\d+$/, '').toLowerCase();
    if (PARTICLE_COLORS[baseName] !== undefined) return PARTICLE_COLORS[baseName];
    // Fall back to type
    const t = (particle.type || '').toLowerCase();
    if (PARTICLE_COLORS[t] !== undefined) return PARTICLE_COLORS[t];
    return 0xaaaaaa;
  }

  function particleRadius(mass) {
    if (!mass || mass <= 0) return BASE_PARTICLE_SIZE * 0.8;
    return BASE_PARTICLE_SIZE * (0.6 + 0.8 * Math.pow(mass, 0.25));
  }

  function isBoson(particle) {
    return (particle.type || '').toLowerCase() === 'boson';
  }

  function isQuark(particle) {
    return (particle.type || '').toLowerCase() === 'quark';
  }

  // ─── Scene Setup ──────────────────────────────────────────
  function initScene() {
    scene = new THREE.Scene();

    // Camera
    camera = new THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 0.1, 2000);
    camera.position.set(20, 15, 20);
    camera.lookAt(0, 0, 0);

    // Renderer
    renderer = new THREE.WebGLRenderer({ antialias: true, alpha: false });
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.toneMapping = THREE.ACESFilmicToneMapping;
    renderer.toneMappingExposure = 1.0;
    DOM.container.appendChild(renderer.domElement);

    // Deep space background gradient (via a large background sphere)
    createSpaceBackground();

    // Star field
    createStarField();

    // Ambient light (very dim)
    const ambientLight = new THREE.AmbientLight(0x1a1a3a, 0.4);
    scene.add(ambientLight);

    // Subtle directional for depth cues
    const dirLight = new THREE.DirectionalLight(0x4466aa, 0.3);
    dirLight.position.set(20, 30, 10);
    scene.add(dirLight);

    // Lattice bounding box (wireframe)
    createLatticeBounds(16);

    // Orbit Controls
    orbitControls = new THREE.OrbitControls(camera, renderer.domElement);
    orbitControls.enableDamping = true;
    orbitControls.dampingFactor = 0.08;
    orbitControls.rotateSpeed = 0.6;
    orbitControls.zoomSpeed = 1.2;
    orbitControls.minDistance = 1;
    orbitControls.maxDistance = 200;
    orbitControls.target.set(8, 8, 8);
    orbitControls.update();
  }

  function createSpaceBackground() {
    const bgGeometry = new THREE.SphereGeometry(900, 64, 64);
    const bgMaterial = new THREE.ShaderMaterial({
      side: THREE.BackSide,
      depthWrite: false,
      uniforms: {
        colorTop:    { value: new THREE.Color(0x0a0a2e) },
        colorBottom: { value: new THREE.Color(0x020208) },
      },
      vertexShader: `
        varying vec3 vWorldPos;
        void main() {
          vec4 worldPosition = modelMatrix * vec4(position, 1.0);
          vWorldPos = worldPosition.xyz;
          gl_Position = projectionMatrix * viewMatrix * worldPosition;
        }
      `,
      fragmentShader: `
        uniform vec3 colorTop;
        uniform vec3 colorBottom;
        varying vec3 vWorldPos;
        void main() {
          float t = clamp((normalize(vWorldPos).y + 1.0) * 0.5, 0.0, 1.0);
          gl_FragColor = vec4(mix(colorBottom, colorTop, t), 1.0);
        }
      `,
    });
    const bgMesh = new THREE.Mesh(bgGeometry, bgMaterial);
    scene.add(bgMesh);
  }

  function createStarField() {
    const positions = new Float32Array(STAR_COUNT * 3);
    const sizes = new Float32Array(STAR_COUNT);
    const colors = new Float32Array(STAR_COUNT * 3);

    for (let i = 0; i < STAR_COUNT; i++) {
      // Random position on a sphere shell
      const theta = Math.random() * Math.PI * 2;
      const phi   = Math.acos(2 * Math.random() - 1);
      const r     = 400 + Math.random() * 400;
      positions[i * 3]     = r * Math.sin(phi) * Math.cos(theta);
      positions[i * 3 + 1] = r * Math.sin(phi) * Math.sin(theta);
      positions[i * 3 + 2] = r * Math.cos(phi);
      sizes[i] = 0.5 + Math.random() * 2.0;
      // Slight color variation (blue-white to warm-white)
      const warmth = Math.random();
      colors[i * 3]     = 0.7 + 0.3 * warmth;
      colors[i * 3 + 1] = 0.7 + 0.2 * warmth;
      colors[i * 3 + 2] = 0.8 + 0.2 * (1 - warmth);
    }

    const starGeo = new THREE.BufferGeometry();
    starGeo.setAttribute('position', new THREE.BufferAttribute(positions, 3));
    starGeo.setAttribute('size',     new THREE.BufferAttribute(sizes, 1));
    starGeo.setAttribute('color',    new THREE.BufferAttribute(colors, 3));

    const starMat = new THREE.ShaderMaterial({
      uniforms: {
        uTime: { value: 0 },
      },
      vertexShader: `
        attribute float size;
        attribute vec3 color;
        varying vec3 vColor;
        varying float vSize;
        uniform float uTime;
        void main() {
          vColor = color;
          vSize = size;
          vec4 mvPosition = modelViewMatrix * vec4(position, 1.0);
          float twinkle = 0.7 + 0.3 * sin(uTime * 0.5 + position.x * 0.1 + position.y * 0.13);
          gl_PointSize = size * twinkle * (300.0 / -mvPosition.z);
          gl_Position = projectionMatrix * mvPosition;
        }
      `,
      fragmentShader: `
        varying vec3 vColor;
        void main() {
          float d = length(gl_PointCoord - vec2(0.5));
          if (d > 0.5) discard;
          float alpha = 1.0 - smoothstep(0.0, 0.5, d);
          gl_FragColor = vec4(vColor, alpha * 0.9);
        }
      `,
      transparent: true,
      depthWrite: false,
      blending: THREE.AdditiveBlending,
    });

    const stars = new THREE.Points(starGeo, starMat);
    stars.userData.isStarField = true;
    scene.add(stars);
  }

  let latticeBounds = null;
  function createLatticeBounds(size) {
    if (latticeBounds) scene.remove(latticeBounds);
    const geo = new THREE.BoxGeometry(size, size, size);
    const edges = new THREE.EdgesGeometry(geo);
    const mat = new THREE.LineBasicMaterial({
      color: 0x2a2a5e,
      transparent: true,
      opacity: 0.3,
    });
    latticeBounds = new THREE.LineSegments(edges, mat);
    latticeBounds.position.set(size / 2, size / 2, size / 2);
    scene.add(latticeBounds);
  }

  // ─── Particle Rendering ───────────────────────────────────
  function createParticleMesh(particle) {
    const group = new THREE.Group();
    group.userData.particleName = particle.name;

    const color = new THREE.Color(resolveColor(particle));
    const radius = particleRadius(particle.mass);
    const isB = isBoson(particle);
    const isQ = isQuark(particle);

    // Core sphere
    const sphereGeo = new THREE.SphereGeometry(radius, 24, 24);
    const sphereMat = new THREE.MeshPhysicalMaterial({
      color: color,
      emissive: color,
      emissiveIntensity: isB ? 0.6 : 0.35,
      metalness: isQ ? 0.4 : 0.1,
      roughness: isB ? 0.9 : 0.4,
      transparent: isB,
      opacity: isB ? 0.55 : 0.95,
    });
    const sphere = new THREE.Mesh(sphereGeo, sphereMat);
    group.add(sphere);

    // Glow aura (additive sprite)
    const glowColor = isQ && particle.color != null
      ? new THREE.Color(COLOR_CHARGE_HUES[particle.color] || resolveColor(particle))
      : color.clone();

    const glowSize = radius * (isQ ? 5 : (isB ? 6 : 3.5));
    const spriteMat = new THREE.SpriteMaterial({
      map: generateGlowTexture(glowColor),
      blending: THREE.AdditiveBlending,
      transparent: true,
      opacity: isB ? 0.3 : 0.5,
      depthWrite: false,
    });
    const glowSprite = new THREE.Sprite(spriteMat);
    glowSprite.scale.set(glowSize, glowSize, 1);
    group.add(glowSprite);

    // Small point light per particle
    const ptLight = new THREE.PointLight(color.getHex(), 0.5, radius * 8, 2);
    group.add(ptLight);

    // Position
    if (particle.pos) {
      group.position.set(particle.pos[0], particle.pos[1], particle.pos[2]);
    }

    scene.add(group);

    const entry = { group, sphere, glow: glowSprite, light: ptLight, data: particle };
    particleMeshes.set(particle.name, entry);

    // Trail
    createTrail(particle.name, color);

    return entry;
  }

  function generateGlowTexture(color) {
    const size = 128;
    const canvas = document.createElement('canvas');
    canvas.width = size;
    canvas.height = size;
    const ctx = canvas.getContext('2d');

    const r = Math.round(color.r * 255);
    const g = Math.round(color.g * 255);
    const b = Math.round(color.b * 255);

    const gradient = ctx.createRadialGradient(size / 2, size / 2, 0, size / 2, size / 2, size / 2);
    gradient.addColorStop(0, `rgba(${r},${g},${b},0.6)`);
    gradient.addColorStop(0.3, `rgba(${r},${g},${b},0.2)`);
    gradient.addColorStop(0.7, `rgba(${r},${g},${b},0.05)`);
    gradient.addColorStop(1, 'rgba(0,0,0,0)');

    ctx.fillStyle = gradient;
    ctx.fillRect(0, 0, size, size);

    const tex = new THREE.CanvasTexture(canvas);
    tex.needsUpdate = true;
    return tex;
  }

  function createTrail(name, color) {
    const maxPoints = TRAIL_LENGTH;
    const geometry = new THREE.BufferGeometry();
    const positions = new Float32Array(maxPoints * 3);
    const alphas = new Float32Array(maxPoints);
    geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
    geometry.setAttribute('alpha', new THREE.BufferAttribute(alphas, 1));

    const material = new THREE.ShaderMaterial({
      uniforms: {
        uColor: { value: color.clone() },
      },
      vertexShader: `
        attribute float alpha;
        varying float vAlpha;
        void main() {
          vAlpha = alpha;
          gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
        }
      `,
      fragmentShader: `
        uniform vec3 uColor;
        varying float vAlpha;
        void main() {
          gl_FragColor = vec4(uColor, vAlpha * 0.6);
        }
      `,
      transparent: true,
      depthWrite: false,
      blending: THREE.AdditiveBlending,
    });

    const line = new THREE.Line(geometry, material);
    scene.add(line);

    particleTrails.set(name, { posHistory: [], line, maxPoints });
  }

  function updateTrail(name, pos) {
    const trail = particleTrails.get(name);
    if (!trail) return;

    trail.posHistory.push([pos.x, pos.y, pos.z]);
    if (trail.posHistory.length > trail.maxPoints) trail.posHistory.shift();

    const positions = trail.line.geometry.attributes.position.array;
    const alphas    = trail.line.geometry.attributes.alpha.array;
    const count     = trail.posHistory.length;

    for (let i = 0; i < trail.maxPoints; i++) {
      if (i < count) {
        const p = trail.posHistory[i];
        positions[i * 3]     = p[0];
        positions[i * 3 + 1] = p[1];
        positions[i * 3 + 2] = p[2];
        alphas[i] = (i + 1) / count; // fade older points
      } else {
        positions[i * 3] = positions[i * 3 + 1] = positions[i * 3 + 2] = 0;
        alphas[i] = 0;
      }
    }

    trail.line.geometry.setDrawRange(0, count);
    trail.line.geometry.attributes.position.needsUpdate = true;
    trail.line.geometry.attributes.alpha.needsUpdate = true;
  }

  function removeParticleMesh(name) {
    const entry = particleMeshes.get(name);
    if (entry) {
      scene.remove(entry.group);
      entry.sphere.geometry.dispose();
      entry.sphere.material.dispose();
      entry.glow.material.map?.dispose();
      entry.glow.material.dispose();
      particleMeshes.delete(name);
    }
    const trail = particleTrails.get(name);
    if (trail) {
      scene.remove(trail.line);
      trail.line.geometry.dispose();
      trail.line.material.dispose();
      particleTrails.delete(name);
    }
  }

  // ─── Force / Coupling Lines ───────────────────────────────
  function clearCouplings() {
    for (const obj of couplingLines) {
      scene.remove(obj);
      obj.geometry.dispose();
      obj.material.dispose();
    }
    couplingLines.length = 0;
  }

  function createCouplingLine(from, to, force, strength) {
    const pFrom = particleMeshes.get(from);
    const pTo   = particleMeshes.get(to);
    if (!pFrom || !pTo) return;

    const forceKey = (force || '').toLowerCase();
    const color = FORCE_COLORS[forceKey] || 0x666688;
    const s = clamp(strength || 0.5, 0.1, 1);

    const posA = pFrom.group.position;
    const posB = pTo.group.position;

    if (forceKey === 'strong') {
      // Neon flux tube — thicker, bright
      const curve = new THREE.CatmullRomCurve3([
        posA.clone(),
        new THREE.Vector3(
          (posA.x + posB.x) / 2 + (Math.random() - 0.5) * 0.8,
          (posA.y + posB.y) / 2 + (Math.random() - 0.5) * 0.8,
          (posA.z + posB.z) / 2 + (Math.random() - 0.5) * 0.8,
        ),
        posB.clone(),
      ]);
      const tubeGeo = new THREE.TubeGeometry(curve, 16, 0.06 * s, 6, false);
      const tubeMat = new THREE.MeshBasicMaterial({
        color: color,
        transparent: true,
        opacity: 0.7 * s,
        blending: THREE.AdditiveBlending,
      });
      const tube = new THREE.Mesh(tubeGeo, tubeMat);
      scene.add(tube);
      couplingLines.push(tube);
    } else if (forceKey === 'em') {
      // Golden field lines — dashed
      const points = [];
      const segments = 24;
      for (let i = 0; i <= segments; i++) {
        const t = i / segments;
        const x = lerp(posA.x, posB.x, t);
        const y = lerp(posA.y, posB.y, t) + Math.sin(t * Math.PI * 3) * 0.3 * s;
        const z = lerp(posA.z, posB.z, t) + Math.cos(t * Math.PI * 3) * 0.3 * s;
        points.push(new THREE.Vector3(x, y, z));
      }
      const lineGeo = new THREE.BufferGeometry().setFromPoints(points);
      const lineMat = new THREE.LineBasicMaterial({
        color: color,
        transparent: true,
        opacity: 0.6 * s,
        blending: THREE.AdditiveBlending,
      });
      const line = new THREE.Line(lineGeo, lineMat);
      scene.add(line);
      couplingLines.push(line);
    } else if (forceKey === 'weak') {
      // Faint halo — simple translucent line
      const lineGeo = new THREE.BufferGeometry().setFromPoints([posA.clone(), posB.clone()]);
      const lineMat = new THREE.LineDashedMaterial({
        color: color,
        transparent: true,
        opacity: 0.25 * s,
        dashSize: 0.3,
        gapSize: 0.2,
        blending: THREE.AdditiveBlending,
      });
      const line = new THREE.Line(lineGeo, lineMat);
      line.computeLineDistances();
      scene.add(line);
      couplingLines.push(line);
    } else {
      // Gravity or unknown — subtle blue distortion line
      const midpoint = posA.clone().add(posB).multiplyScalar(0.5);
      midpoint.y += 0.4 * s;
      const curve = new THREE.QuadraticBezierCurve3(posA.clone(), midpoint, posB.clone());
      const curvePoints = curve.getPoints(20);
      const lineGeo = new THREE.BufferGeometry().setFromPoints(curvePoints);
      const lineMat = new THREE.LineBasicMaterial({
        color: color,
        transparent: true,
        opacity: 0.2 * s,
        blending: THREE.AdditiveBlending,
      });
      const line = new THREE.Line(lineGeo, lineMat);
      scene.add(line);
      couplingLines.push(line);
    }
  }

  // ─── Frame Processing ─────────────────────────────────────
  function processFrame(frame) {
    if (!frame) return;

    latestFrame = frame;
    currentTick = frame.tick || 0;

    // Update lattice bounds if size changed
    if (frame.lattice_size && latticeBounds) {
      const s = frame.lattice_size;
      latticeBounds.scale.set(1, 1, 1);
      latticeBounds.geometry.dispose();
      const geo = new THREE.BoxGeometry(s, s, s);
      const edges = new THREE.EdgesGeometry(geo);
      latticeBounds.geometry = edges;
      latticeBounds.position.set(s / 2, s / 2, s / 2);
    }

    // Track which particles are still present
    const activeNames = new Set();

    // Update / create particles
    if (frame.particles) {
      for (const p of frame.particles) {
        activeNames.add(p.name);
        let entry = particleMeshes.get(p.name);

        if (!entry) {
          entry = createParticleMesh(p);
        }

        // Smooth position interpolation using frac_vel
        if (p.pos) {
          const target = new THREE.Vector3(p.pos[0], p.pos[1], p.pos[2]);
          // Add fractional velocity for sub-tick smoothing
          if (p.vel) {
            target.x += p.vel[0] * 0.5;
            target.y += p.vel[1] * 0.5;
            target.z += p.vel[2] * 0.5;
          }
          entry.group.position.lerp(target, 0.25);
        }

        // Update data reference
        entry.data = p;

        // Boson pulsing
        if (isBoson(p)) {
          const t = clock.getElapsedTime();
          const pulse = 0.4 + 0.15 * Math.sin(t * 3 + p.name.length);
          entry.sphere.material.opacity = pulse;
          entry.glow.material.opacity = pulse * 0.4;
        }

        // Update trail
        updateTrail(p.name, entry.group.position);
      }
    }

    // Remove particles that are gone
    for (const name of particleMeshes.keys()) {
      if (!activeNames.has(name)) {
        if (focusedParticle === name) unfocusParticle();
        removeParticleMesh(name);
      }
    }

    // Couplings
    clearCouplings();
    if (frame.couplings) {
      for (const c of frame.couplings) {
        createCouplingLine(c.from, c.to, c.force, c.strength);
      }
    }

    // Update HUD
    updateHUD(frame);

    // Update focused particle info
    if (focusedParticle) {
      const entry = particleMeshes.get(focusedParticle);
      if (entry) updateParticleInfo(entry.data);
    }
  }

  // ─── HUD Updates ──────────────────────────────────────────
  function updateHUD(frame) {
    DOM.hudTick.textContent    = frame.tick || 0;
    DOM.hudSpeed.textContent   = formatSpeed(speedMultiplier);
    DOM.hudCount.textContent   = frame.particles ? frame.particles.length : 0;
    DOM.tickCounter.textContent = frame.tick || 0;

    // Energy
    if (frame.invariants && frame.invariants.total_energy != null) {
      DOM.hudEnergy.textContent = String(frame.invariants.total_energy);
    }

    // Invariants
    if (frame.invariants) {
      let html = '';
      for (const [key, val] of Object.entries(frame.invariants)) {
        if (key === 'total_energy') continue;
        const isBool = typeof val === 'boolean';
        const dotClass = isBool ? (val ? 'ok' : 'fail') : 'neutral';
        const display = key.replace(/_/g, ' ');
        const valStr = isBool ? (val ? '✓' : '✗') : String(val);
        html += `<div class="invariant-row">
          <span class="invariant-dot ${dotClass}"></span>
          <span class="invariant-name">${display}: ${valStr}</span>
        </div>`;
      }
      DOM.hudInvariants.innerHTML = html || '<div class="invariant-row"><span class="invariant-dot neutral"></span><span class="invariant-name">No invariants</span></div>';
    }

    // Events
    if (frame.events && frame.events.length > 0) {
      const recent = frame.events.slice(-MAX_EVENTS);
      DOM.hudEvents.innerHTML = recent
        .map(e => `<div class="event-item">${escapeHtml(e)}</div>`)
        .join('');
    }
  }

  function escapeHtml(str) {
    const div = document.createElement('div');
    div.textContent = str;
    return div.innerHTML;
  }

  // ─── Particle Info Panel ──────────────────────────────────
  function focusParticle(name) {
    const entry = particleMeshes.get(name);
    if (!entry) return;

    focusedParticle = name;
    updateParticleInfo(entry.data);
    DOM.particleInfo.style.display = 'block';

    // Move camera towards particle
    if (cameraMode === 'orbit') {
      orbitControls.target.lerp(entry.group.position, 0.5);
    }
  }

  function unfocusParticle() {
    focusedParticle = null;
    DOM.particleInfo.style.display = 'none';
  }

  function updateParticleInfo(p) {
    DOM.infoName.textContent  = p.name || '—';
    DOM.infoType.textContent  = p.type || '—';
    DOM.infoState.textContent = p.state || '—';
    DOM.infoMass.textContent  = p.mass != null ? p.mass.toFixed(6) : '—';
    DOM.infoGen.textContent   = p.gen != null ? p.gen : '—';
    DOM.infoPos.textContent   = p.pos ? `[${p.pos.map(v => v.toFixed ? v.toFixed(1) : v).join(', ')}]` : '—';
    DOM.infoVel.textContent   = p.vel ? `[${p.vel.map(v => v.toFixed ? v.toFixed(1) : v).join(', ')}]` : '—';
    DOM.infoColor.textContent = p.color != null ? `charge ${p.color}` : 'n/a';
  }

  // ─── Camera Controls ──────────────────────────────────────
  function toggleCameraMode() {
    if (cameraMode === 'orbit') {
      cameraMode = 'fly';
      orbitControls.enabled = false;
      DOM.cameraModeText.textContent = 'FLY';
      renderer.domElement.requestPointerLock();
    } else {
      cameraMode = 'orbit';
      orbitControls.enabled = true;
      DOM.cameraModeText.textContent = 'ORBIT';
      document.exitPointerLock();
    }
  }

  function updateFlyCamera(dt) {
    if (cameraMode !== 'fly') return;

    const speed = 12 * dt;
    const dir = new THREE.Vector3();
    camera.getWorldDirection(dir);
    const right = new THREE.Vector3().crossVectors(dir, camera.up).normalize();

    if (keysDown.has('w') || keysDown.has('W')) camera.position.addScaledVector(dir, speed);
    if (keysDown.has('s') || keysDown.has('S')) camera.position.addScaledVector(dir, -speed);
    if (keysDown.has('d') || keysDown.has('D')) camera.position.addScaledVector(right, speed);
    if (keysDown.has('a') || keysDown.has('A')) camera.position.addScaledVector(right, -speed);
    if (keysDown.has(' '))                      camera.position.y += speed;
    if (keysDown.has('Shift'))                   camera.position.y -= speed;
  }

  // ─── WebSocket ────────────────────────────────────────────
  function connectWebSocket() {
    DOM.connText.textContent = 'Connecting…';
    DOM.connStatus.classList.remove('connected');

    try {
      ws = new WebSocket(WS_URL);
    } catch (e) {
      scheduleReconnect();
      return;
    }

    ws.onopen = () => {
      DOM.connText.textContent = 'Connected';
      DOM.connStatus.classList.add('connected');
    };

    ws.onmessage = (evt) => {
      try {
        const frame = JSON.parse(evt.data);
        if (playing || pendingStep) {
          processFrame(frame);
          pendingStep = false;
        }
      } catch (e) {
        console.warn('SFTOE: Bad frame', e);
      }
    };

    ws.onclose = () => {
      DOM.connText.textContent = 'Disconnected';
      DOM.connStatus.classList.remove('connected');
      scheduleReconnect();
    };

    ws.onerror = () => {
      ws.close();
    };
  }

  function scheduleReconnect() {
    setTimeout(connectWebSocket, RECONNECT_DELAY_MS);
  }

  function sendCommand(cmd) {
    if (ws && ws.readyState === WebSocket.OPEN) {
      ws.send(JSON.stringify(cmd));
    }
  }

  // ─── Time Controls ────────────────────────────────────────
  function setupTimeControls() {
    DOM.btnPlay.addEventListener('click', () => {
      playing = !playing;
      DOM.btnPlay.textContent = playing ? '⏸' : '▶';
      DOM.btnPlay.classList.toggle('playing', playing);
      sendCommand({ action: playing ? 'play' : 'pause', speed: speedMultiplier });
    });

    DOM.btnStep.addEventListener('click', () => {
      pendingStep = true;
      sendCommand({ action: 'step' });
    });

    DOM.speedSlider.addEventListener('input', (e) => {
      // Logarithmic scale: 0..5 → 1..100000
      const v = parseFloat(e.target.value);
      speedMultiplier = Math.round(Math.pow(10, v));
      if (speedMultiplier < 1) speedMultiplier = 1;
      DOM.speedDisplay.textContent = formatSpeed(speedMultiplier);
      DOM.hudSpeed.textContent = formatSpeed(speedMultiplier);
      sendCommand({ action: 'speed', speed: speedMultiplier });
    });

    // Set initial state
    DOM.btnPlay.textContent = '⏸';
    DOM.btnPlay.classList.add('playing');
  }

  // ─── Input Events ─────────────────────────────────────────
  function setupInputEvents() {
    // Keyboard
    window.addEventListener('keydown', (e) => {
      keysDown.add(e.key);
      if (e.key === 'f' || e.key === 'F') {
        e.preventDefault();
        toggleCameraMode();
      }
      if (e.key === 'Escape') {
        if (focusedParticle) unfocusParticle();
        if (cameraMode === 'fly') toggleCameraMode();
      }
    });

    window.addEventListener('keyup', (e) => {
      keysDown.delete(e.key);
    });

    // Mouse look for fly mode
    document.addEventListener('mousemove', (e) => {
      if (cameraMode !== 'fly') return;
      if (!document.pointerLockElement) return;

      const sensitivity = 0.002;
      const euler = new THREE.Euler(0, 0, 0, 'YXZ');
      euler.setFromQuaternion(camera.quaternion);
      euler.y -= e.movementX * sensitivity;
      euler.x -= e.movementY * sensitivity;
      euler.x = clamp(euler.x, -Math.PI / 2 + 0.01, Math.PI / 2 - 0.01);
      camera.quaternion.setFromEuler(euler);
    });

    // If pointer lock is lost, go back to orbit
    document.addEventListener('pointerlockchange', () => {
      if (!document.pointerLockElement && cameraMode === 'fly') {
        cameraMode = 'orbit';
        orbitControls.enabled = true;
        DOM.cameraModeText.textContent = 'ORBIT';
      }
    });

    // Particle picking via click
    renderer.domElement.addEventListener('click', onCanvasClick);

    // Close particle info
    DOM.infoClose.addEventListener('click', unfocusParticle);

    // Resize
    window.addEventListener('resize', onWindowResize);
  }

  function onCanvasClick(event) {
    // Skip if in fly mode or if user is dragging
    if (cameraMode === 'fly') return;

    const rect = renderer.domElement.getBoundingClientRect();
    mouseNDC.x =  ((event.clientX - rect.left) / rect.width)  * 2 - 1;
    mouseNDC.y = -((event.clientY - rect.top)  / rect.height) * 2 + 1;

    raycaster.setFromCamera(mouseNDC, camera);

    // Collect all sphere meshes
    const targets = [];
    for (const [name, entry] of particleMeshes) {
      targets.push(entry.sphere);
      entry.sphere.userData.particleName = name;
    }

    const intersects = raycaster.intersectObjects(targets, false);
    if (intersects.length > 0) {
      const hit = intersects[0].object;
      focusParticle(hit.userData.particleName);
    } else {
      unfocusParticle();
    }
  }

  function onWindowResize() {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
  }

  // ─── Animation Loop ───────────────────────────────────────
  function animate() {
    requestAnimationFrame(animate);

    const dt = clock.getDelta();
    const elapsed = clock.getElapsedTime();

    // Update star twinkle
    scene.traverse((obj) => {
      if (obj.isPoints && obj.userData.isStarField && obj.material.uniforms) {
        obj.material.uniforms.uTime.value = elapsed;
      }
    });

    // Boson pulsing animation (continuous even when paused)
    for (const [name, entry] of particleMeshes) {
      if (entry.data && isBoson(entry.data)) {
        const pulse = 0.35 + 0.2 * Math.sin(elapsed * 2.5 + name.length * 0.7);
        entry.sphere.material.opacity = pulse;
        entry.sphere.material.emissiveIntensity = 0.4 + 0.3 * Math.sin(elapsed * 3 + name.length);
        entry.glow.material.opacity = pulse * 0.35;
      }

      // Subtle glow breathing for all particles
      const breathe = 1.0 + 0.08 * Math.sin(elapsed * 1.5 + name.length * 0.3);
      entry.glow.scale.setScalar(entry.glow.scale.x > 0 ? entry.glow.scale.x : 1);
      entry.light.intensity = 0.4 + 0.15 * Math.sin(elapsed * 2 + name.length * 0.5);
    }

    // Focused particle camera tracking
    if (focusedParticle && cameraMode === 'orbit') {
      const entry = particleMeshes.get(focusedParticle);
      if (entry) {
        orbitControls.target.lerp(entry.group.position, 0.05);
      }
    }

    // Fly camera
    updateFlyCamera(dt);

    // Orbit controls update
    if (cameraMode === 'orbit') {
      orbitControls.update();
    }

    renderer.render(scene, camera);
  }

  // ─── Demo Mode (for when no WebSocket data is available) ──
  function generateDemoFrame(tick) {
    const latticeSize = 16;
    const t = tick * 0.02;
    const particles = [
      {
        name: 'electron_1', state: '1/4',
        pos: [8 + 4 * Math.cos(t), 8 + 2 * Math.sin(t * 1.3), 8 + 3 * Math.sin(t * 0.7)],
        type: 'lepton', gen: 1, mass: 0.0025, vel: [0, 0, 1], color: null,
      },
      {
        name: 'electron_2', state: '1/4',
        pos: [8 + 3 * Math.cos(t * 0.8 + 2), 8 + 3 * Math.sin(t * 0.6 + 1), 8 + 2 * Math.cos(t * 1.1)],
        type: 'lepton', gen: 1, mass: 0.0025, vel: [1, 0, 0], color: null,
      },
      {
        name: 'muon_1', state: '1/4',
        pos: [4 + 3 * Math.sin(t * 0.9), 12 + 2 * Math.cos(t * 0.5), 10 + 2 * Math.sin(t * 0.8)],
        type: 'lepton', gen: 2, mass: 0.55, vel: [0, 1, 0], color: null,
      },
      {
        name: 'u_quark_1', state: '1/7',
        pos: [5 + 2 * Math.sin(t * 1.2), 5 + 2 * Math.cos(t * 0.9), 5 + Math.sin(t * 1.5)],
        type: 'quark', gen: 1, mass: 0.012, vel: [1, 0, 0], color: 1,
      },
      {
        name: 'u_quark_2', state: '2/7',
        pos: [6 + 2 * Math.cos(t * 1.1), 5 + Math.sin(t * 1.3), 6 + 2 * Math.cos(t * 0.8)],
        type: 'quark', gen: 1, mass: 0.012, vel: [0, 1, 0], color: 2,
      },
      {
        name: 'd_quark_1', state: '3/7',
        pos: [5 + Math.sin(t * 0.7 + 1), 6 + 2 * Math.cos(t * 1.0), 5 + 2 * Math.sin(t * 1.2)],
        type: 'quark', gen: 1, mass: 0.025, vel: [0, 0, 1], color: 3,
      },
      {
        name: 'photon_1', state: '1/1',
        pos: [8 + 6 * Math.cos(t * 2), 8 + 6 * Math.sin(t * 2), 8],
        type: 'boson', gen: 0, mass: 0, vel: [1, 1, 0], color: null,
      },
      {
        name: 'gluon_1', state: '1/1',
        pos: [5.5 + Math.sin(t * 1.5) * 0.5, 5.5 + Math.cos(t * 1.5) * 0.5, 5.5],
        type: 'boson', gen: 0, mass: 0, vel: [0, 0, 0], color: null,
      },
      {
        name: 'tau_1', state: '1/4',
        pos: [12 + 2 * Math.cos(t * 0.4), 4 + 3 * Math.sin(t * 0.6), 12 + 2 * Math.cos(t * 0.9)],
        type: 'lepton', gen: 3, mass: 9.3, vel: [0, -1, 0], color: null,
      },
    ];

    const couplings = [
      { from: 'u_quark_1', to: 'u_quark_2', force: 'strong', strength: 0.857 },
      { from: 'u_quark_2', to: 'd_quark_1', force: 'strong', strength: 0.72 },
      { from: 'u_quark_1', to: 'd_quark_1', force: 'strong', strength: 0.65 },
      { from: 'electron_1', to: 'electron_2', force: 'em', strength: 0.45 },
      { from: 'electron_1', to: 'u_quark_1', force: 'em', strength: 0.3 },
      { from: 'muon_1', to: 'tau_1', force: 'weak', strength: 0.2 },
      { from: 'electron_1', to: 'muon_1', force: 'gravity', strength: 0.05 },
    ];

    const events = [
      'photon_1 emitted from electron_1',
      'gluon_1 exchanged between u_quark_1 and d_quark_1',
      `electron_1 coupled to electron_2 via EM`,
    ];

    return {
      tick: tick,
      lattice_size: latticeSize,
      particles: particles,
      couplings: couplings,
      invariants: {
        energy_conserved: true,
        total_energy: '15/16',
        momentum_conserved: true,
        charge_conserved: true,
      },
      events: events,
    };
  }

  let demoTick = 0;
  let demoInterval = null;

  function startDemoMode() {
    // Run demo mode if WebSocket isn't connected after timeout
    if (demoInterval) return;
    demoInterval = setInterval(() => {
      if (ws && ws.readyState === WebSocket.OPEN) {
        clearInterval(demoInterval);
        demoInterval = null;
        return;
      }
      if (playing) {
        demoTick++;
        processFrame(generateDemoFrame(demoTick));
      }
    }, 33); // ~30 fps demo
  }

  // ─── Initialization ───────────────────────────────────────
  function init() {
    cacheDom();
    initScene();
    setupTimeControls();
    setupInputEvents();
    connectWebSocket();
    animate();

    // Start demo mode after a brief delay if no WebSocket data arrives
    setTimeout(startDemoMode, 2000);
  }

  // Start when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
