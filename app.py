from flask import Flask, jsonify
from flask_pydantic_spec import FlaskPydanticSpec
import datetime
from datetime import datetime
from dateutil.relativedelta import relativedelta

app = Flask(__name__)

spec = FlaskPydanticSpec ( 'flask',
                           tittle = 'First API - SENAI',
                           version = '1.0.0',)
spec.register(app)

@app.route('/<tipo>/<quantidade>')

def validade(tipo, quantidade):
    """
    #Endpoint:
    'GET /verificar_data/<ano>-<mes>-<dia>'

    :param tipo: tipo de tempo(dias,semanas,meses e ano)
    :param quantidade:  quantidades de tempo de validade até a data de fabricação.
    :return:

    #Resposta (JSON)
    {
            'fabricacao': 10/09/2023,
            'validade': 31/03/2026,
        }

    #Erros Possíveis:
    {"erro": "Valor inválido."}

    """

    try:
        prazo = int(quantidade)
        meses = datetime.today()+relativedelta(months=prazo)
        # years=
        anos = datetime.today()+relativedelta(years=prazo)
        # weeks=
        semanas = datetime.today()+relativedelta(weeks=prazo)
        # days=
        dias = datetime.today()+relativedelta(days=prazo)

        if tipo == 'meses':
            validade = meses
        elif tipo == 'anos':
            validade = anos
        elif tipo == 'semanas':
            validade = semanas
        elif tipo == 'dias':
            validade = dias

        return jsonify({
            'Fabricacao': datetime.today().strftime('%d/%m/%Y'),
            'Validade': validade.strftime('%d/%m/%Y'),
        })

    except ValueError:
        return jsonify({
            'erro':'valor inválido'
        })


if __name__ == '__main__':
    app.run(debug=True)