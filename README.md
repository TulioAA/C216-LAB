AgroManutenção
Sistema de Controle de Manutenção de Máquinas Agrícolas desenvolvido para a disciplina C216 - Sistemas Distribuídos.

Objetivo
Auxiliar no gerenciamento de máquinas agrícolas, permitindo o cadastro de máquinas e o acompanhamento da necessidade de manutenção com base nas horas trabalhadas.

Funcionalidades Implementadas
Máquinas
Cadastro de máquinas agrícolas
Listagem de máquinas cadastradas
Identificação automática de manutenção atrasada
Regra de Negócio
Uma máquina é considerada com manutenção atrasada quando:

horas_trabalhadas >= horas_proxima_manutencao

Nesse caso, o sistema retorna:

manutencao_atrasada = true