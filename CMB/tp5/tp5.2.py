def smith_waterman(seq1, seq2, match=2, mismatch=-1, gap_penalty=-1):
    # Inicialização da matriz de pontuações
    rows, cols = len(seq1) + 1, len(seq2) + 1
    matrix = [[0] * cols for _ in range(rows)]

    # Preenchimento da matriz de acordo com as regras do algoritmo
    for i in range(1, rows):
        for j in range(1, cols):
            match_score = matrix[i-1][j-1] + (match if seq1[i-1] == seq2[j-1] else mismatch)
            delete_score = matrix[i-1][j] + gap_penalty
            insert_score = matrix[i][j-1] + gap_penalty

            matrix[i][j] = max(0, match_score, delete_score, insert_score)

    # Encontrar a pontuação máxima na matriz
    max_score = 0
    max_i, max_j = 0, 0
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] > max_score:
                max_score = matrix[i][j]
                max_i, max_j = i, j

    # Reconstruir o alinhamento a partir da posição da pontuação máxima
    align1, align2 = "", ""
    i, j = max_i, max_j
    while matrix[i][j] != 0:
        if matrix[i][j] == matrix[i-1][j-1] + (match if seq1[i-1] == seq2[j-1] else mismatch):
            align1 = seq1[i-1] + align1
            align2 = seq2[j-1] + align2
            i -= 1
            j -= 1
        elif matrix[i][j] == matrix[i-1][j] + gap_penalty:
            align1 = seq1[i-1] + align1
            align2 = '-' + align2
            i -= 1
        elif matrix[i][j] == matrix[i][j-1] + gap_penalty:
            align1 = '-' + align1
            align2 = seq2[j-1] + align2
            j -= 1

    return align1, align2, max_score

# Exemplo de uso
seq1 = "GACATAT"
seq2 = "ACTAGAG"
alignment1, alignment2, score = smith_waterman(seq1, seq2)

print("Sequencia 1:", alignment1)
print("Sequencia 2:", alignment2)
print("Pontuacao:", score)

print("\n" + "="*40 + "\n")


# DNA_samples = [
#     "ACCATACCTTCGATTGTCGTGGCCACCCTCGGATTACACGGCAGAGGTGC",
#     "GTTGTGTTCCGATAGGCCAGCATATTATCCTAAGGCGTTACCCCAATCGA",
#     "TTTTCCGTCGGATTTGCTATAGCCCCTGAACGCTACATGCACGAAACCAC",
#     "AGTTATGTATGCACGTCATCAATAGGACATAGCCTTGTAGTTAACAG",
#     "TGTAGCCCGGCCGTACAGTAGAGCCTTCACCGGCATTCTGTTTG",
#     "ATTAAGTTATTTCTATTACAGCAAAACGATCATATGCAGATCCGCAGTGCGCT",
#     "GGTAGAGACACGTCCACCTAAAAAAGTGA",
#     "ATGATTATCATGAGTGCCCGGCTGCTCTGTAATAGGGACCCGTTATGGTCGTGTTCGATCAGAGCGCTCTA",
#     "TACGAGCAGTCGTATGCTTTCTCGAATTCCGTGCGGTTAAGCGTGACAGA",
#     "TCCCAGTGCACAAAACGTGATGGCAGTCCATGCGATCATACGCAAT",
#     "GGTCTCCAGACACCGGCGCACCAGTTTTCACGCCGAAAGCATC",
#     "AGAAGGATAACGAGGAGCACAAATGAGAGTGTTTGAACTGGACCTGTAGTTTCTCTG",
#     "ACGAAGAAACCCACCTTGAGCTGTTGCGTTGTTGCGCTGCCTAGATGCAGTGG",
#     "TAACTGCGCCAAAACGTCTTCCAATCCCCTTATCCAATTTAACTCACCGC",
#     "AATTCTTACAATTTAGACCCTAATATCACATCATTAGACACTAATTGCCT",
#     "TCTGCCAAAATTCTGTCCACAAGCGTTTTAGTTCGCCCCAGTAAAGTTGT",
#     "TCAATAACGACCACCAAATCCGCATGTTACGGGACTTCTTATTAATTCTA",
#     "TTTTTCGTGGGGAGCAGCGGATCTTAATGGATGGCGCCAGGTGGTATGGA",
# ]

# for i in range(len(DNA_samples)):
#     for j in range(i + 1, len(DNA_samples)):
#         alignment1, alignment2, score = smith_waterman(DNA_samples[i], DNA_samples[j])
#         print(f"Alinhamento entre Sequencia {i+1} e Sequencia {j+1}:\n")
#         print("Pontuacao:", score)
#         print("\n" + "="*40 + "\n")