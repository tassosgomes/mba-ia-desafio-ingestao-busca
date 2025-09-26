from search import search_prompt

def main():
    print("Digite sua pergunta ou use 'sair' para finalizar o chat.")
    print("-" * 50)
    
    while True:
        try:
            question = input("\nDigite sua pergunta: ").strip()
            
            if question.lower() in ['sair']:
                print("\n Encerrando o chat")
                break
            
            if not question:
                print("Por favor, digite uma pergunta válida.")
                continue
            
            print("\nAguarde...")
            answer = search_prompt(question)
            
            print(f"\nResposta:\n{answer}")
            print("-" * 50)
            
        except KeyboardInterrupt:
            print("\nChat encerrado pelo usuário")
            break
        except Exception as e:
            print(f"\nErro inesperado: {e}")
            print("Tente novamente ou digite 'sair' para finalizar.")

if __name__ == "__main__":
    main()