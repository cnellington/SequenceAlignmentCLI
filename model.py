"""
Caleb Ellington
CSE 427: Computational Biology
01/25/2020
"""


class Alignment:
    """
    inputs:
    file1   first sequence to align
    file2   second sequence to align
    protein flag to use BLOSUM62 scoring
    """

    def __init__(self, file1, file2, protein):
        self._file1 = file1
        self._file2 = file2
        self._protein = protein
        self._load()

    def _load(self):
        with open(self._file1, 'r') as sequence_file:
            self._seq1 = sequence_file.read()
        with open(self._file2, 'r') as sequence_file:
            self._seq2 = sequence_file.read()
        if self._protein:
            # Load BLOSUM62 matrix
            pass

    def run_needleman_wunsch(self):
        raise NotImplementedError

    def run_smith_waterman(self):
        raise NotImplementedError


