import mathemedica as mm
# ============================== test 1==================================
# matrix1=[
#   [1,2,3],
#   [4,5,6]
# ]
# matrix2=[
#   [4,6,8],
#   [12,14,15],
# ]
# result_matrix=mm.times_matrices(matrix1,matrix2)
# for row in result_matrix:
#   print(f" {row}")

matrix1=[
  [1,2,3,4],
  [5,6,7,8],
  [9,10,11,12]
]
matrix2=[
  [1,2],
  [3,4],
  [5,6],
  [7,8]
]

result_matrix=mm.times_matrices(matrix1,matrix2)
for row in result_matrix:
  print(f" {row}")