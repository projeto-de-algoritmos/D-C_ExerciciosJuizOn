# https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/

class Solution(object):
    def numOfWays(self, nums):
        """
        :type nums: Lista[int]
        :rtype: int
        """

        def comb(n, k):
            # Calcula n escolha k módulo MOD
            numerador = 1
            denominador = 1

            for i in range(k):
                numerador = (numerador * (n - i)) % MOD
                denominador = (denominador * (i + 1)) % MOD

            return (numerador * pow(denominador, MOD - 2, MOD)) % MOD

        MOD = 10**9 + 7

        def contar_formas(nums):
            if len(nums) <= 1:
                return 1

            esquerda = [x for x in nums if x < nums[0]]
            direita = [x for x in nums if x > nums[0]]

            contagem_esquerda = contar_formas(esquerda)
            contagem_direita = contar_formas(direita)

            n = len(esquerda) + len(direita)

            # Calcula o número de maneiras de escolher elementos da esquerda e da direita
            # e multiplica pelo número de maneiras de organizar os elementos restantes
            resultado = comb(n, len(esquerda)) * contagem_esquerda * contagem_direita
            return resultado % MOD

        
        return contar_formas(nums) - 1  # Subtrai 1 para excluir a ordenação original
