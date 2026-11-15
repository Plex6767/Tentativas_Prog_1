# Questão 2. Tratamento dos dados de temperatura.
#
# Você deve preparar um script que verifique se existem dados faltantes
# (ou inválidos) de temperaturas. Se este for o caso, seu script deve
# substituir dados faltantes pela média dos primeiros valores válidos
# imediatamente antes e após o(s) dado(s) faltante(s).
# Utilize apenas temperaturas de bulbo seco.
#
# Você deve preparar
# uma função que receba um dado completo de temperatura
# horária para 2025 e retorne uma matriz com a média diária de temperatura,
# e também qual a temperatura máxima e mínima atingida no dia. Você deve
# verificar também em que hora do dia a temperatura atinge seu máximo, e a
# que hora atinge seu mínimo. Cada linha da matriz deve ser um dia, cada
# coluna uma das informações (temperatura média, máxima e mínima diárias,
# horário da temp. máxima, horário da temp. mínima). Esta matriz deve ser
# salva em um arquivo texto (formato csv).