from models.utilisateur import Utilisateur

utilisateur1 = Utilisateur(1, "SAMAKE", "Adama", "samake@gmail.com", "+22899595766", 20, "Zanguera", "patient", "M",
                           "123456", "1.3902U049U290U+1.1231U93I13112")
utilisateur2 = Utilisateur(2, "ABALO", "Koffi", "abalo@gmail.com", "+22899595760", 22, "Zanguera", "patient", "M",
                           "123456", "1.3902U049U290U+1.1231U93I13112")
utilisateur3 = Utilisateur(3, "AMAH", "Kwatcha", "amah@gmail.com", "+22899435766", 36, "Avedji", "medecin", "F",
                           "123456", "1.3902U049U290U+1.1231U93I13112")
utilisateur4 = Utilisateur(4, "AKA", "Kossi", "aka@gmail.com", "+22899995766", 20, "Zanguera", "patient", "M", "123456",
                           "1.3902U049U290U+1.1231U93I13112")
utilisateur5 = Utilisateur(5, "AMAKE", "Adam", "amake@gmail.com", "+22890595766", 40, "Zanguera", "medecin", "M",
                           "123456", "1.3902U049U290U+1.1231U93I13112")
utilisateur6 = Utilisateur(6, "MOKE", "Regis", "moke@gmail.com", "+22899095766", 33, "Tsevie", "medecin", "M", "123456",
                           "1.3902U049U290U+1.1231U93I13112")

utilisateurs = [
    utilisateur1.to_json(),
    utilisateur2.to_json(),
    utilisateur3.to_json(),
    utilisateur4.to_json(),
    utilisateur5.to_json(),
    utilisateur6.to_json(),
]


def get_all_users():
    return utilisateurs


def get_user(id):
    for utilisateur in utilisateurs:
        if utilisateur['id'] == id:
            return utilisateur
    return {}
