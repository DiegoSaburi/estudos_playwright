# Estudos Playwright

Projeto de automação de testes com Python, Playwright e pytest.

## Arquitetura do projeto

A estrutura foi organizada para separar responsabilidades por funcionalidade e manter os testes enxutos.

```text
.
├── conftest.py              # Fixtures globais do pytest
├── pytest.ini               # Configuração do pytest
├── requirements.txt         # Dependências do projeto
├── README.md                # Documentação do projeto
├── fixtures/                # Fixtures customizadas e utilitários de ambiente
├── pages/
│   ├── qa_playground/
│   │   ├── page.py          # Page Object principal da página de formulário
│   │   └── sections/        # Seções da página (login, personal info, address, interests, password)
│   └── todo/
│       ├── page.py          # Page Object principal da página TodoMVC
│       └── sections/        # Seções da página (novo item, lista, filtros)
├── tests/
│   └── test_example.py      # Testes de exemplo da aplicação
└── .venv/                   # Ambiente virtual do projeto
```

### O que cada pasta faz

#### `pages/`
Centraliza os Page Objects e suas seções. Aqui fica a representação da interface da página testada.

- `pages/<feature>/page.py`: representa a página completa.
- `pages/<feature>/sections/`: contém blocos menores da página, como formulário, lista, filtros ou outros componentes reutilizáveis.

Essa divisão ajuda a manter cada classe com uma responsabilidade clara e evita que todos os seletores fiquem misturados em um único arquivo.

#### `tests/`
Contém os testes de comportamento. Os testes devem chamar os Page Objects e descrever a ação do usuário, sem depender de detalhes de implementação do HTML.

#### `fixtures/`
Pode guardar fixtures específicas, helpers e utilitários reutilizáveis para cenários mais complexos.

No projeto atual, a maioria dos fixtures está em `conftest.py`, mas essa pasta fica disponível para crescimento.

#### `conftest.py`
Responsável por criar os fixtures do pytest, como por exemplo:

- `playwright_page`: página genérica para testes de site externo
- `todo_page`: Page Object da página TodoMVC
- `qa_playground_form_page`: Page Object da página de formulário

Esses fixtures deixam os testes mais legíveis e evitam repetição de setup.

---

## Como adicionar uma nova página para testar

Siga este passo a passo:

### 1) Crie a pasta da funcionalidade dentro de `pages/`

Exemplo:

```text
pages/
└── checkout/
```

### 2) Crie o Page Object principal

Dentro da pasta da funcionalidade, crie um arquivo `page.py`.

Exemplo:

```python
from playwright.sync_api import Page

from pages.checkout.sections.shipping import ShippingSection
from pages.checkout.sections.payment import PaymentSection


class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.shipping = ShippingSection(page)
        self.payment = PaymentSection(page)
```

### 3) Crie as seções da página

Se a página tiver blocos distintos, crie uma pasta `sections/` e divida a lógica por responsabilidade.

Exemplo:

```text
pages/
└── checkout/
    ├── page.py
    └── sections/
        ├── shipping.py
        └── payment.py
```

### 4) Defina os seletores e ações nas seções

Cada seção deve ter apenas o que faz parte daquele bloco da página.

Exemplo:

```python
from playwright.sync_api import Page


class ShippingSection:
    def __init__(self, page: Page):
        self.street = page.get_by_label("Street")
        self.city = page.get_by_label("City")

    def fill(self, street: str = "", city: str = "") -> None:
        self.street.fill(street)
        self.city.fill(city)
```

### 5) Adicione o fixture no `conftest.py`

Isso permite que o teste receba um objeto já pronto e navegando na página correta.

```python
@pytest.fixture
def checkout_page(page: Page) -> CheckoutPage:
    page.goto("https://exemplo.com/checkout")
    return CheckoutPage(page)
```

### 6) Crie o teste em `tests/`

O teste deve descrever a jornada do usuário, usando o Page Object.

```python
from pages.checkout.page import CheckoutPage


def test_submit_checkout(checkout_page: CheckoutPage):
    checkout_page.shipping.fill(
        street="Main Street",
        city="Springfield",
    )
    checkout_page.payment.fill(
        card_number="1234567890123456",
        name="Ned Stark",
    )
```

### 7) Mantenha os testes simples e de negócio

Os testes não devem ficar cheios de detalhes de CSS, IDs ou manipulação cara a cara com o DOM. A ideia é deixar o código assim:

- dado um cenário
- o teste chama o page object
- o page object executa a ação
- o teste valida o comportamento esperado

---

## Boas práticas da arquitetura aqui aplicada

- Cada funcionalidade tem sua própria pasta em `pages/`
- Cada página é composta por seções menores
- Seletores ficam encapsulados nos Page Objects
- Testes focam em comportamento e fluxo do usuário
- Fixtures ajudam a reduzir duplicação de setup
- A estrutura cresce por funcionalidade, não por tipo de elemento genérico

---

## Executar os testes

```bash
pytest
```

Ou para um arquivo específico:

```bash
pytest tests/test_example.py
```

## Instalação

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
playwright install
```

Esse padrão facilita manter o projeto organizado conforme vai crescendo e ajuda muito na reutilização de código entre páginas e cenários.

