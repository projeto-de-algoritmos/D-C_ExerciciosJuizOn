# https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        def ExotericSelect(lista):
            # Função para calcular a mediana de uma lista
            def calcular_mediana(sublista):
                sublista_ordenada = sorted(sublista)
                tamanho = len(sublista_ordenada)
                return sublista_ordenada[tamanho // 2]

            # Dividir a lista em sublistas de até 5 elementos
            sublistas = [lista[i:i+5] for i in range(0, len(lista), 5)]

            # Calcular as medianas das sublistas
            medianas = [calcular_mediana(sublista) for sublista in sublistas]
            # Se houver apenas uma mediana, retorna ela
            if len(medianas) <= 1:
                return medianas[0]
            else:
                # Caso contrário, chama recursivamente a função com as medianas como entrada
                return ExotericSelect(medianas)


        def MoM(lista, k):
            mediana = ExotericSelect(lista)
            esquerda=[]
            direita=[]

            for i in lista:
                if i < mediana:
                    esquerda.append(i)
                elif i > mediana:
                    direita.append(i)

            esquerda.append(mediana)

            if len(lista)-len(esquerda) == k-1 or k < 0 or len(lista) <= 2:
                return mediana
            elif len(lista)-len(esquerda) < k:
                return MoM(direita, k-len(esquerda)-1)
            else:
                return MoM(esquerda, k)

        nums = nums1 + nums2

        if len(nums) == 2:
            return (float(nums[0])+float(nums[1]))/2
        elif len(nums) % 2 == 0: 
            mediana = float(MoM(nums, (len(nums)//2)))
            mediana2 = float(MoM(nums, len(nums)//2-1))
            print(mediana,mediana2)
            mediana = (mediana2+mediana)/2
        else:
            mediana = MoM(nums, 1+len(nums)//2)
        return mediana
