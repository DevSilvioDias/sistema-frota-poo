# 🚗 Sistema de Gestão de Frota (POO em Python)

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge)

Projeto prático desenvolvido em **Python** com o objetivo de consolidar os pilares da **Programação Orientada a Objetos (POO)** aplicados a um sistema de controle de veículos.

---

## 🎯 Funcionalidades

- Cadastro de diferentes tipos de veículos (**Carros** e **Motos**) a partir de uma classe base comum.
- Controle de estado de ignição (`Ligado` / `Desligado`) com proteção de atributo interno.
- Exibição formatada e personalizada de cada veículo no terminal.

---

## 🧠 Conceitos de POO Aplicados

- **Classes e Objetos:** Modelagem de entidades do mundo real (`Veiculo`, `Carro`, `Moto`).
- **Encapsulamento:** Uso de atributo protegido (`_ligado`) alterado apenas por método específico (`alternar_ignicao()`).
- **Herança e `super()`:** Reaproveitamento de atributos e comportamentos da superclasse `Veiculo` nas subclasses.
- **Polimorfismo:** Sobrescrita e extensão do método especial `__str__` para adaptar a saída de cada tipo de veículo.

---

## 📂 Estrutura do Projeto

```text
sistema-frota-poo/
├── app.py      # Definição das classes Veiculo, Carro e Moto
├── main.py     # Ponto de entrada e execução da frota
└── README.md   # Documentação do projeto
