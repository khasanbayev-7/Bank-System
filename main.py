from command_interface import Command
from commands.register_command import RegisterCommand
from commands.login_command import LoginCommand
from commands.balance_command import BalanceCommand
from commands.user_command import UserCommand
from commands.add_card_command import AddCardCommand
from commands.transfer_command import TransferCommand
from commands.update_profile_command import UpdateProfileCommand
from commands.admin_panel_command import AdminPanelCommand
from commands.show_users_command import ShowUsersCommand
from commands.register_admin_command import RegisterAdminCommand 

commands = {
    "register": RegisterCommand(),
    "login": LoginCommand(),
    "balance": BalanceCommand(),
    "user": UserCommand(),
    "add_card": AddCardCommand(),
    "transfer": TransferCommand(),
    "update_profile": UpdateProfileCommand(),
    "admin": AdminPanelCommand(),
    "show_users": ShowUsersCommand(),
    "admin_register": RegisterAdminCommand(),
}

while True:
    cmd = input("Buyruq kiriting (register/admin_register/login/balance/add_card/transfer/update_profile/exit): ").strip()

    if cmd == "exit":
        break

    if cmd == "admin_register":
        print("❌ Bu buyruq siz uchun mumkin emas!")
        continue

    if cmd in commands:
        commands[cmd].execute()
    else:
        print("Noto‘g‘ri buyruq kiritildi!")
