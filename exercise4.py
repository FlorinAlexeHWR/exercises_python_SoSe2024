
# =============================================================================
# quad_zahl =[]
# 
# for k in range(1, 11):
#     if k % 2 != 0:
#         quad_zahl.append(k ** 2)
#     else:
#         quad_zahl.append(k)
#         
# print(quad_zahl)
# =============================================================================
  
quad_zahl = [k**2 if k%2 !=0 else k**2 for k in range (1,11)]

print(quad_zahl)