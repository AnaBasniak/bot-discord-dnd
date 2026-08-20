from mini_mestre.data.popular_racas import popular_racas
from mini_mestre.data.popular_subracas import popular_subracas
from mini_mestre.data.popular_bonus_raciais import popular_bonus_raciais
from mini_mestre.data.popular_caracteristicas_raciais import (
    popular_caracteristicas_raciais,
)
from mini_mestre.data.popular_escolhas_raciais import (
    popular_escolhas_raciais,
)

from mini_mestre.data.popular_classes import popular_classes
from mini_mestre.data.popular_dados_classes import (
    popular_dados_classes,
)
from mini_mestre.data.popular_proficiencias_classes import (
    popular_proficiencias_classes,
)
from mini_mestre.data.popular_subclasses import popular_subclasses
from mini_mestre.data.popular_caracteristicas_classes import (
    popular_caracteristicas_classes,
)
from mini_mestre.data.popular_caracteristicas_subclasses import (
    popular_caracteristicas_subclasses,
)

from mini_mestre.data.popular_antecedentes import (
    popular_antecedentes,
)
from mini_mestre.data.popular_dados_antecedentes import (
    popular_dados_antecedentes,
)
from mini_mestre.data.popular_caracteristicas_antecedentes import (
    popular_caracteristicas_antecedentes,
)

from mini_mestre.data.popular_equipamentos import (
    popular_equipamentos,
)
from mini_mestre.data.popular_equipamentos_classes import (
    popular_equipamentos_classes,
)


def executar_etapa(
    numero,
    nome,
    funcao,
):
    print()
    print(
        "=" * 60
    )
    print(
        f"[{numero}] {nome}"
    )
    print(
        "=" * 60
    )

    funcao()


def popular_tudo():

    etapas = [
        (
            "Raças",
            popular_racas,
        ),
        (
            "Sub-raças",
            popular_subracas,
        ),
        (
            "Bônus raciais",
            popular_bonus_raciais,
        ),
        (
            "Características raciais",
            popular_caracteristicas_raciais,
        ),
        (
            "Escolhas raciais",
            popular_escolhas_raciais,
        ),

        (
            "Classes",
            popular_classes,
        ),
        (
            "Salvaguardas e perícias das classes",
            popular_dados_classes,
        ),
        (
            "Proficiências das classes",
            popular_proficiencias_classes,
        ),
        (
            "Subclasses",
            popular_subclasses,
        ),
        (
            "Progressão das classes",
            popular_caracteristicas_classes,
        ),
        (
            "Características das subclasses",
            popular_caracteristicas_subclasses,
        ),

        (
            "Antecedentes",
            popular_antecedentes,
        ),
        (
            "Dados dos antecedentes",
            popular_dados_antecedentes,
        ),
        (
            "Características dos antecedentes",
            popular_caracteristicas_antecedentes,
        ),

        (
            "Equipamentos",
            popular_equipamentos,
        ),
        (
            "Equipamentos das classes",
            popular_equipamentos_classes,
        ),
    ]

    print()
    print(
        "Iniciando povoamento do banco do Mini Mestre..."
    )

    for numero, etapa in enumerate(
        etapas,
        start=1
    ):

        nome = etapa[0]
        funcao = etapa[1]

        executar_etapa(
            numero,
            nome,
            funcao,
        )

    print()
    print(
        "=" * 60
    )
    print(
        "BANCO POPULADO COM SUCESSO!"
    )
    print(
        "=" * 60
    )


if __name__ == "__main__":
    popular_tudo()