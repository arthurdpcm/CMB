DNA_samples = [
    "ACCATACCTTCGATTGTCGTGGCCACCCTCGGATTACACGGCAGAGGTGC",
    "GTTGTGTTCCGATAGGCCAGCATATTATCCTAAGGCGTTACCCCAATCGA",
    "TTTTCCGTCGGATTTGCTATAGCCCCTGAACGCTACATGCACGAAACCAC",
    "AGTTATGTATGCACGTCATCAATAGGACATAGCCTTGTAGTTAACAG",
    "TGTAGCCCGGCCGTACAGTAGAGCCTTCACCGGCATTCTGTTTG",
    "ATTAAGTTATTTCTATTACAGCAAAACGATCATATGCAGATCCGCAGTGCGCT",
    "GGTAGAGACACGTCCACCTAAAAAAGTGA",
    "ATGATTATCATGAGTGCCCGGCTGCTCTGTAATAGGGACCCGTTATGGTCGTGTTCGATCAGAGCGCTCTA",
    "TACGAGCAGTCGTATGCTTTCTCGAATTCCGTGCGGTTAAGCGTGACAGA",
    "TCCCAGTGCACAAAACGTGATGGCAGTCCATGCGATCATACGCAAT",
    "GGTCTCCAGACACCGGCGCACCAGTTTTCACGCCGAAAGCATC",
    "AGAAGGATAACGAGGAGCACAAATGAGAGTGTTTGAACTGGACCTGTAGTTTCTCTG",
    "ACGAAGAAACCCACCTTGAGCTGTTGCGTTGTTGCGCTGCCTAGATGCAGTGG",
    "TAACTGCGCCAAAACGTCTTCCAATCCCCTTATCCAATTTAACTCACCGC",
    "AATTCTTACAATTTAGACCCTAATATCACATCATTAGACACTAATTGCCT",
    "TCTGCCAAAATTCTGTCCACAAGCGTTTTAGTTCGCCCCAGTAAAGTTGT",
    "TCAATAACGACCACCAAATCCGCATGTTACGGGACTTCTTATTAATTCTA",
    "TTTTTCGTGGGGAGCAGCGGATCTTAATGGATGGCGCCAGGTGGTATGGA",
]

def hamming_distance(str1, str2):
  if len(str1) != len(str2):
    return -1
  else:
    distance = 0
    for i in range(len(str1)):
      if str1[i] != str2[i]:
        distance += 1
    return distance
    


print(hamming_distance(DNA_samples[0], DNA_samples[1]))

import numpy as np



def levenshtein_distance(str1, str2):

  if not str1 or not str2:
    return max(len(str1), len(str2))

  n = len(str1)
  m = len(str2)

  # Cria a matriz de distância.
  matrix = np.zeros((n + 1, m + 1))

  # Inicializa a matriz de distância.
  for i in range(n + 1):
    matrix[i][0] = i
  for j in range(m + 1):
    matrix[0][j] = j

  # Calcula a distância de Levenshtein.
  for i in range(1, n + 1):
    for j in range(1, m + 1):
      if str1[i - 1] == str2[j - 1]:
        matrix[i][j] = matrix[i - 1][j - 1]
      else:
        matrix[i][j] = min(
            matrix[i - 1][j] + 1,
            matrix[i][j - 1] + 1,
            matrix[i - 1][j - 1] + 1,
        )

  # Retorna a distância de Levenshtein.
  return matrix[n][m]

print(levenshtein_distance(DNA_samples[0], DNA_samples[1]))

matrix = []

for i in range(len(DNA_samples)):
  matrix.append([])
  for j in range(len(DNA_samples)):
      matrix[i].append(levenshtein_distance(DNA_samples[i], DNA_samples[j]))



open("matrix.txt", "w").write(str(matrix))


