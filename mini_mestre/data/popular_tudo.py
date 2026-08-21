from mini_mestre.data.popular_racas import (
    popular_racas,
)

from mini_mestre.data.popular_subracas import (
    popular_subracas,
)

from mini_mestre.data.popular_bonus_raciais import (
    popular_bonus_raciais,
)

from mini_mestre.data.popular_caracteristicas_raciais import (
    popular_caracteristicas_raciais,
)

from mini_mestre.data.popular_escolhas_raciais import (
    popular_escolhas_raciais,
)

from mini_mestre.data.popular_classes import (
    popular_classes,
)

from mini_mestre.data.popular_subclasses import (
    popular_subclasses,
)

from mini_mestre.data.popular_dados_classes import (
    popular_dados_classes,
)

from mini_mestre.data.popular_proficiencias_classes import (
    popular_proficiencias_classes,
)

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

from mini_mestre.data.popular_magias import (
    popular_magias,
)

from mini_mestre.data.popular_magias_classes import (
    popular_magias_classes,
)

from mini_mestre.data.popular_slots_magia import (
    popular_slots_magia,
)


def popular_tudo():

    print(
        "\n=============================="
    )

    print(
        "INICIANDO POPULAÇÃO DO BANCO"
    )

    print(
        "=============================="
    )


    # =====================================================
    # RAÇAS
    # =====================================================

    print(
        "\n=== POPULANDO RAÇAS ==="
    )

    popular_racas()


    print(
        "\n=== POPULANDO SUB-RAÇAS ==="
    )

    popular_subracas()


    print(
        "\n=== POPULANDO BÔNUS RACIAIS ==="
    )

    popular_bonus_raciais()


    print(
        "\n=== POPULANDO CARACTERÍSTICAS RACIAIS ==="
    )

    popular_caracteristicas_raciais()


    print(
        "\n=== POPULANDO ESCOLHAS RACIAIS ==="
    )

    popular_escolhas_raciais()


    # =====================================================
    # CLASSES
    # =====================================================

    print(
        "\n=== POPULANDO CLASSES ==="
    )

    popular_classes()


    print(
        "\n=== POPULANDO SUBCLASSES ==="
    )

    popular_subclasses()


    print(
        "\n=== POPULANDO DADOS DAS CLASSES ==="
    )

    popular_dados_classes()


    print(
        "\n=== POPULANDO PROFICIÊNCIAS DAS CLASSES ==="
    )

    popular_proficiencias_classes()


    print(
        "\n=== POPULANDO CARACTERÍSTICAS DAS CLASSES ==="
    )

    popular_caracteristicas_classes()


    print(
        "\n=== POPULANDO CARACTERÍSTICAS DAS SUBCLASSES ==="
    )

    popular_caracteristicas_subclasses()


    # =====================================================
    # ANTECEDENTES
    # =====================================================

    print(
        "\n=== POPULANDO ANTECEDENTES ==="
    )

    popular_antecedentes()


    print(
        "\n=== POPULANDO DADOS DOS ANTECEDENTES ==="
    )

    popular_dados_antecedentes()


    print(
        "\n=== POPULANDO CARACTERÍSTICAS DOS ANTECEDENTES ==="
    )

    popular_caracteristicas_antecedentes()


    # =====================================================
    # EQUIPAMENTOS
    # =====================================================

    print(
        "\n=== POPULANDO EQUIPAMENTOS ==="
    )

    popular_equipamentos()


    print(
        "\n=== POPULANDO EQUIPAMENTOS DAS CLASSES ==="
    )

    popular_equipamentos_classes()


    # =====================================================
    # MAGIAS
    # =====================================================

    print(
        "\n=== POPULANDO MAGIAS ==="
    )

    popular_magias()


    print(
        "\n=== ASSOCIANDO MAGIAS ÀS CLASSES ==="
    )

    popular_magias_classes()


    print(
        "\n=== POPULANDO SLOTS DE MAGIA ==="
    )

    popular_slots_magia()


    # =====================================================
    # FINAL
    # =====================================================

    print(
        "\n=============================="
    )

    print(
        "BANCO POPULADO COM SUCESSO!"
    )

    print(
        "=============================="
    )


if __name__ == "__main__":
    popular_tudo()