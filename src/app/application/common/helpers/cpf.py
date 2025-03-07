from validate_docbr import CPF

class CPFHelper:
    @staticmethod
    def validate(cpf: str) -> bool:
        return CPF().validate(cpf)