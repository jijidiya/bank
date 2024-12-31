"""
Module bancaire simulant la gestion de comptes bancaires.

Ce module définit une classe `BankAccount` pour gérer des opérations
bancaires telles que les dépôts, les retraits et les transferts entre comptes.
Il inclut également une exception personnalisée `BalanceException`.
"""


class BalanceException(Exception):
    """
    Exception levée lorsqu'une transaction depasse le solde disponible
    """
    pass





class BankAccount:
    """
    Représente un compte bancaire avec des fonctionnalités de base telles que
    la vérification du solde, les dépôts, les retraits et les transferts.
    
    Attributs:
        balance (float): Le solde actuel du compte.
        name (str): Le nom associé au compte.
    """

    def __init__(self, initial_amount, acct_name):
        """
        Initialise un compte bancaire avec un solde initial et un nom.
        
        Args:
            initial_amount (float): Le montant initial du solde du compte.
            acct_name (str): Le nom associé au compte.
        """
        self.balance = initial_amount
        self.name = acct_name

    def get_acct_data(self):
        """
        Affiche les informations de base du compte (nom et balance)
        """
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")
         
    def get_balance(self):
        """
        retourne le solde actuel du compte

        Returns:
            float: le solde actuel du compte
        """
        return self.balance

    def deposit(self, amount):
        """
        Ajoute un montant au solde du compte

        Args:
            amount(float): le montant à deposer 
        """
        self.balance += amount

    def viable_transaction(self, amount):
        """
        Vérifie si une transaction est viable en fonction du solde du compte.
        
        Args:
            amount (float): Le montant de la transaction.
        
        Raises:
            BalanceException: Si le solde est insuffisant pour effectuer la transaction.
        """

        #verifie la balance du solde est suffisante pour la transaction
        if self.balance >= amount:
            return
        else:
            #si non, leve une exception personnalisée avec un message explicatif
            raise BalanceException(
                f"\nSorry, account'{self.name}' only has a balance of ${self.balance:.2f}"
            )

    def withdraw(self, amount):
        """
        Retire un montant du solde si les fonds sont suffisants.
        
        Args:
            amount (float): Le montant à retirer.
        
        Exceptions:
            BalanceException: Si le solde est insuffisant.
        """
        try:
            self.viable_transaction(amount)
            self.balance -= amount
        except BalanceException as error:
            print(f'\n withdraw interrupted: {error}')

    def transfert(self, amount, account):
        """
        Transfère un montant d'un compte à un autre.
        
        Args:
            amount (float): Le montant à transférer.
            account (BankAccount): Le compte destinataire.
        """
        try:
            self.withdraw(amount)
            account.deposit(amount)
        except BalanceException as error:
            print(f'transfert interrupted : {error}')
        
    
class InterestRewardsAcct(BankAccount):
    """
    Représente un compte bancaire avec des récompenses sur les dépôts.
    
    Cette classe hérite de BankAccount et applique une récompense de 5 % 
    sur chaque dépôt effectué.
    """
    
    def deposit(self, amount):
        """
        Dépose un montant dans le compte avec une récompense de 5 %.
        
        Args:
            amount (float): Le montant à déposer.
        
        Exemple:
            Si vous déposez 100.00, le solde augmentera de 105.00 (100 + 5 %).
        """
        if amount <= 0:
            raise ValueError("the deposit amount must be positive")
        self.balance += (amount*1.05)
