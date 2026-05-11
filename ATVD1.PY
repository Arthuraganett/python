app = Flask(__name__) 

@app.route('/')
def ola_mundo():
    return 'Decorator, oque é?' 

@app.route('/decorator') 
def hello():
    return 'Decorators são um padrão de projeto estrutural, comuns em linguagens como Python e TypeScript, que permitem adicionar novos comportamentos a objetos, métodos ou classes existentes de forma dinâmica, sem alterar o código-fonte original. Eles "embrulham" o código original, permitindo executar ações antes ou depois da sua execução.' # Isso é o que será retornado quando a rota '/hello' for acessada

if __name__ == '__main__':
    app.run(debug=True) 