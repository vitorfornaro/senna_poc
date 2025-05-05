from dataclasses import asdict
import json
import os
from interface.cliente_modal import Bancario, Cliente
from utils.utils import nif_validation


def extraiDadosCliente(data: Cliente):
    try:
        checkNif = nif_validation(data.nif)
        if(checkNif):
          bancario = data.bancario[0]  # Pega o primeiro item do array bancario

          cliente = Cliente(
              nome=data.nome,
              nif=data.nif,
              bancario=[
                  Bancario(
                      mesMapa=bancario.mesMapa,
                      instituicao=bancario.instituicao,
                      divida=bancario.divida,
                      parcela=bancario.parcela,
                      garantias=bancario.garantias,
                      num_devedores=bancario.num_devedores,
                      prod_financeiro=bancario.prod_financeiro,
                      entrada_incumpr=bancario.entrada_incumpr,
                      data_inicio=bancario.data_inicio,
                      data_fim=bancario.data_fim,
                  )
              ],
          )

          cliente_dict = asdict(cliente)

          folderCustomers = "customers"

          if not os.path.exists(folderCustomers):
              # To DO - Criar um log de pasta criada
              os.makedirs(folderCustomers)

          with open(folderCustomers + "/" + data.nif + ".json", "w", encoding="utf-8") as f:
              json.dump(cliente_dict, f, ensure_ascii=False, indent=2)

          print("Cliente salvo com sucesso!")
        else:
            # To DO - Criar um log de erro alertando que o NIF não é valido
            print("NIF não é válido!")

    except Exception as e:
        # To DO - Criar um log de erro e remover o print
        print("Error:", e)
