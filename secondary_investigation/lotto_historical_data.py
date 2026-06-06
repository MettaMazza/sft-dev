"""
UK National Lottery (Lotto) Historical Draw Results
====================================================
69 consecutive draws from 1st October 2025 to 6th June 2026.
UK Lotto: 6 main balls drawn from 1-59, plus 1 bonus ball from remaining 53.
Draws held every Wednesday and Saturday.

Data sourced from lottery.co.uk archive pages and cross-referenced
with independent.co.uk, echo-news.co.uk, and lotto.net.

Format: list of dicts ordered from newest to oldest.
Each dict has:
  - 'date': human-readable date string
  - 'main': sorted list of 6 main balls
  - 'bonus': the bonus ball number
"""

DRAWS = [
    # === June 2026 ===
    {'date': '6th June 2026',    'main': [8, 10, 26, 30, 35, 42],  'bonus': 50},
    {'date': '3rd June 2026',    'main': [7, 10, 20, 55, 57, 59],  'bonus': 44},

    # === May 2026 ===
    {'date': '30th May 2026',    'main': [4, 17, 18, 20, 23, 56],  'bonus': 33},
    {'date': '27th May 2026',    'main': [33, 36, 38, 46, 47, 50], 'bonus': 35},
    {'date': '23rd May 2026',    'main': [4, 5, 6, 7, 11, 33],     'bonus': 35},
    {'date': '20th May 2026',    'main': [9, 20, 24, 51, 52, 59],  'bonus': 31},
    {'date': '16th May 2026',    'main': [4, 21, 23, 27, 36, 57],  'bonus': 20},
    {'date': '13th May 2026',    'main': [9, 12, 15, 16, 37, 39],  'bonus': 14},
    {'date': '9th May 2026',     'main': [3, 11, 13, 14, 43, 49],  'bonus': 5},
    {'date': '6th May 2026',     'main': [7, 31, 33, 37, 39, 56],  'bonus': 20},
    {'date': '2nd May 2026',     'main': [3, 4, 6, 12, 29, 40],    'bonus': 19},

    # === April 2026 ===
    {'date': '29th April 2026',  'main': [4, 14, 22, 32, 38, 52],  'bonus': 27},
    {'date': '25th April 2026',  'main': [3, 10, 14, 19, 32, 53],  'bonus': 23},
    {'date': '22nd April 2026',  'main': [6, 12, 18, 29, 49, 56],  'bonus': 7},
    {'date': '18th April 2026',  'main': [1, 4, 12, 15, 39, 47],   'bonus': 48},
    {'date': '15th April 2026',  'main': [22, 45, 49, 53, 54, 56], 'bonus': 25},
    {'date': '11th April 2026',  'main': [7, 10, 14, 15, 17, 35],  'bonus': 31},
    {'date': '8th April 2026',   'main': [27, 29, 34, 36, 43, 59], 'bonus': 37},
    {'date': '4th April 2026',   'main': [15, 16, 23, 32, 42, 46], 'bonus': 52},
    {'date': '1st April 2026',   'main': [7, 16, 23, 27, 35, 40],  'bonus': 48},

    # === March 2026 ===
    {'date': '28th March 2026',  'main': [9, 24, 35, 40, 47, 52],  'bonus': 18},
    {'date': '25th March 2026',  'main': [19, 22, 31, 32, 34, 40], 'bonus': 43},
    {'date': '21st March 2026',  'main': [5, 10, 18, 28, 34, 53],  'bonus': 46},
    {'date': '18th March 2026',  'main': [14, 16, 18, 22, 47, 56], 'bonus': 54},
    {'date': '14th March 2026',  'main': [10, 30, 36, 44, 45, 58], 'bonus': 59},
    {'date': '11th March 2026',  'main': [2, 3, 18, 25, 40, 54],   'bonus': 14},
    {'date': '7th March 2026',   'main': [9, 37, 39, 40, 47, 51],  'bonus': 19},
    {'date': '4th March 2026',   'main': [20, 33, 43, 46, 50, 56], 'bonus': 45},

    # === February 2026 ===
    {'date': '28th February 2026', 'main': [12, 15, 22, 28, 31, 32], 'bonus': 23},
    {'date': '25th February 2026', 'main': [31, 34, 36, 41, 54, 57], 'bonus': 27},
    {'date': '21st February 2026', 'main': [2, 14, 24, 33, 37, 40],  'bonus': 19},
    {'date': '18th February 2026', 'main': [1, 11, 12, 13, 18, 49],  'bonus': 33},
    {'date': '14th February 2026', 'main': [10, 13, 27, 50, 54, 56], 'bonus': 14},
    {'date': '11th February 2026', 'main': [5, 11, 28, 30, 47, 53],  'bonus': 52},
    {'date': '7th February 2026',  'main': [7, 25, 27, 46, 52, 59],  'bonus': 40},
    {'date': '4th February 2026',  'main': [1, 2, 19, 29, 51, 57],   'bonus': 5},

    # === January 2026 ===
    {'date': '31st January 2026',  'main': [7, 8, 17, 25, 37, 40],   'bonus': 11},
    {'date': '28th January 2026',  'main': [33, 45, 50, 52, 58, 59], 'bonus': 15},
    {'date': '24th January 2026',  'main': [1, 4, 8, 23, 34, 57],    'bonus': 29},
    {'date': '21st January 2026',  'main': [5, 24, 28, 46, 49, 56],  'bonus': 19},
    {'date': '17th January 2026',  'main': [12, 26, 30, 32, 39, 58], 'bonus': 4},
    {'date': '14th January 2026',  'main': [2, 5, 22, 35, 44, 54],   'bonus': 23},
    {'date': '10th January 2026',  'main': [5, 6, 13, 18, 22, 53],   'bonus': 9},
    {'date': '7th January 2026',   'main': [3, 9, 20, 33, 45, 50],   'bonus': 12},
    {'date': '3rd January 2026',   'main': [6, 20, 34, 38, 47, 48],  'bonus': 4},

    # === December 2025 ===
    {'date': '31st December 2025', 'main': [3, 20, 27, 29, 38, 46],  'bonus': 14},
    {'date': '27th December 2025', 'main': [20, 36, 40, 43, 51, 55], 'bonus': 21},
    {'date': '24th December 2025', 'main': [12, 15, 16, 35, 38, 48], 'bonus': 49},
    {'date': '20th December 2025', 'main': [2, 25, 27, 34, 45, 52],  'bonus': 47},
    {'date': '17th December 2025', 'main': [15, 20, 43, 50, 51, 58], 'bonus': 36},
    {'date': '13th December 2025', 'main': [18, 22, 24, 41, 53, 56], 'bonus': 59},
    {'date': '10th December 2025', 'main': [4, 9, 26, 35, 42, 46],   'bonus': 38},
    {'date': '6th December 2025',  'main': [5, 7, 10, 17, 32, 42],   'bonus': 40},
    {'date': '3rd December 2025',  'main': [6, 13, 19, 48, 57, 58],  'bonus': 1},

    # === November 2025 ===
    {'date': '29th November 2025', 'main': [2, 6, 9, 16, 38, 48],    'bonus': 46},
    {'date': '26th November 2025', 'main': [10, 21, 49, 54, 55, 56], 'bonus': 40},
    {'date': '22nd November 2025', 'main': [9, 11, 14, 43, 49, 59],  'bonus': 35},
    {'date': '19th November 2025', 'main': [15, 18, 36, 50, 51, 57], 'bonus': 10},
    {'date': '15th November 2025', 'main': [9, 11, 27, 44, 48, 52],  'bonus': 25},
    {'date': '12th November 2025', 'main': [9, 17, 31, 34, 47, 58],  'bonus': 23},
    {'date': '8th November 2025',  'main': [2, 3, 42, 45, 46, 47],   'bonus': 44},
    {'date': '5th November 2025',  'main': [2, 15, 20, 42, 43, 59],  'bonus': 16},
    {'date': '1st November 2025',  'main': [17, 18, 31, 36, 39, 51], 'bonus': 29},

    # === October 2025 ===
    {'date': '29th October 2025',  'main': [9, 24, 30, 33, 35, 54],  'bonus': 32},
    {'date': '25th October 2025',  'main': [4, 9, 28, 40, 42, 59],   'bonus': 55},
    {'date': '22nd October 2025',  'main': [3, 24, 26, 34, 35, 36],  'bonus': 9},
    {'date': '18th October 2025',  'main': [6, 39, 43, 52, 58, 59],  'bonus': 19},
    {'date': '15th October 2025',  'main': [29, 33, 36, 38, 48, 58], 'bonus': 52},
    {'date': '11th October 2025',  'main': [11, 17, 25, 31, 51, 54], 'bonus': 53},
    {'date': '8th October 2025',   'main': [2, 21, 42, 48, 56, 57],  'bonus': 51},
    {'date': '4th October 2025',   'main': [6, 8, 12, 33, 49, 59],   'bonus': 42},
    {'date': '1st October 2025',   'main': [13, 28, 31, 39, 51, 59], 'bonus': 27},
]

# Total draws in this dataset
TOTAL_DRAWS = len(DRAWS)  # 69
