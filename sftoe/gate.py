import ast
import os

class SFTOEGateError(SyntaxError):
    """Raised when SFTOE syntactic rules are violated."""
    pass

class SmithianASTValidator(ast.NodeVisitor):
    def __init__(self, filename=None, is_core=False):
        self.filename = filename
        self.is_core = is_core
        # If the file path is known, determine if it is a core/test file
        if filename:
            basename = os.path.basename(filename)
            # Core and tests are allowed to use basic math/subtraction to construct test asserts and implement primitives
            if basename in ["core.py", "proof.py", "test_sftoe.py"]:
                self.is_core = True

    def visit_Num(self, node):
        if node.n == 0:
            raise SFTOEGateError(
                f"Syntactic violation: Literal zero is forbidden in SFTOE. Found '0' on line {node.lineno}."
            )
        self.generic_visit(node)

    def visit_Constant(self, node):
        # Python 3.8+ representation
        if node.value == 0 or node.value == 0.0:
            # Booleans (True, False) subclass int, so False == 0. Allow explicit False.
            if not isinstance(node.value, bool):
                raise SFTOEGateError(
                    f"Syntactic violation: Literal zero is forbidden in SFTOE. Found '{node.value}' on line {getattr(node, 'lineno', '?')}."
                )
        self.generic_visit(node)

    def visit_BinOp(self, node):
        if isinstance(node.op, ast.Sub):
            if not self.is_core:
                raise SFTOEGateError(
                    f"Syntactic violation: Bare subtraction '-' is forbidden. "
                    f"Use 'take(big, small)' or 'cast_out(x)'. Line {node.lineno}."
                )
        self.generic_visit(node)

    def visit_UnaryOp(self, node):
        if isinstance(node.op, ast.USub):
            if not self.is_core:
                raise SFTOEGateError(
                    f"Syntactic violation: Unary negation '-' is forbidden in SFTOE. Line {node.lineno}."
                )
        self.generic_visit(node)

    def visit_Call(self, node):
        func_name = ""
        if isinstance(node.func, ast.Name):
            func_name = node.func.id
        elif isinstance(node.func, ast.Attribute):
            func_name = node.func.attr
        
        banned_funcs = {
            "sqrt", "sin", "cos", "tan", "log", "exp", "asin", "acos", "atan", "sinh", "cosh", "tanh",
            "eval", "exec", "globals", "locals", "__import__", "getattr", "setattr", "delattr"
        }
        if func_name in banned_funcs:
            raise SFTOEGateError(
                f"Syntactic violation: Forbidden apparatus or dynamic execution call '{func_name}' is banned. Line {node.lineno}."
            )
        self.generic_visit(node)

    def visit_Import(self, node):
        if not self.is_core:
            banned_modules = {"math", "cmath", "numpy", "scipy", "sys", "os", "importlib", "builtins"}
            for alias in node.names:
                mod_base = alias.name.split('.')[0]
                if mod_base in banned_modules:
                    raise SFTOEGateError(
                        f"Syntactic violation: Importing forbidden library '{alias.name}' is banned. Line {node.lineno}."
                    )
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        if not self.is_core:
            banned_modules = {"math", "cmath", "numpy", "scipy", "sys", "os", "importlib", "builtins"}
            if node.module:
                mod_base = node.module.split('.')[0]
                if mod_base in banned_modules:
                    raise SFTOEGateError(
                        f"Syntactic violation: Importing from forbidden library '{node.module}' is banned. Line {node.lineno}."
                    )
        self.generic_visit(node)

    def visit_Attribute(self, node):
        if not self.is_core:
            banned_attrs = {"__dict__", "__globals__", "__code__", "__func__", "__self__", "__module__"}
            if node.attr in banned_attrs:
                raise SFTOEGateError(
                    f"Syntactic violation: Access to internal attribute '{node.attr}' is forbidden. Line {node.lineno}."
                )
        self.generic_visit(node)

    def visit_Assign(self, node):
        if not self.is_core:
            for target in node.targets:
                self._check_assignment_target(target)
        self.generic_visit(node)

    def visit_AnnAssign(self, node):
        if not self.is_core:
            self._check_assignment_target(node.target)
        self.generic_visit(node)

    def _check_assignment_target(self, target):
        protected = {"verify_value", "verify_hypothesis_orbit", "fold", "take", "cast_out", "ONE", "SmithianValue"}
        if isinstance(target, ast.Name):
            if target.id in protected:
                raise SFTOEGateError(
                    f"Syntactic violation: Redefining protected SFTOE primitive '{target.id}' is forbidden. Line {target.lineno}."
                )
        elif isinstance(target, ast.Attribute):
            if target.attr in protected:
                raise SFTOEGateError(
                    f"Syntactic violation: Overriding protected SFTOE attribute '{target.attr}' is forbidden. Line {target.lineno}."
                )

def verify_code(code_str, filename=None, is_core=False):
    """
    Statically analyzes code_str using AST.
    Raises SFTOEGateError if any syntactic violations are found.
    """
    try:
        tree = ast.parse(code_str, filename=filename or "<string>")
    except SyntaxError as e:
        raise SFTOEGateError(f"Syntax error in code: {e}")
    
    visitor = SmithianASTValidator(filename=filename, is_core=is_core)
    visitor.visit(tree)
    return True

def verify_file(filepath):
    """
    Statically analyzes a python file.
    Raises SFTOEGateError if any syntactic violations are found.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    return verify_code(content, filename=filepath)
