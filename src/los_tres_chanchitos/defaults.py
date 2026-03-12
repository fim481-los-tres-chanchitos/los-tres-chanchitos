from los_tres_chanchitos.models import Pig, Scenario, Wolf


def original_scenario() -> Scenario:
    return Scenario(
        pigs=[
            Pig(
                material="paja",
                personality="tenía prisa",
                house_description="se levanta rápido, pero es poco resistente.",
                blows_to_fall=1,
            ),
            Pig(
                material="madera",
                personality="dispuesto a trabajar un poco más",
                house_description="se levanta con más trabajo, aunque puede romperse.",
                blows_to_fall=2,
            ),
            Pig(
                material="ladrillos",
                personality="paciente",
                house_description="se levanta con tiempo y esfuerzo, pero es sólida y segura.",
                blows_to_fall=None,
            ),
        ],
        wolf=Wolf(
            blows_limit=3,
        ),
    )
