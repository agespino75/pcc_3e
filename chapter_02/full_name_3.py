first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)

favorite_language = "python "
favorite_language = favorite_language.rstrip()
print(favorite_language)

favorite_language = " python "
favorite_language.rstrip()
favorite_language.lstrip()
favorite_language.strip()
print(favorite_language.strip())

nostarch_url = 'https://nostarch.com'
simple_url =nostarch_url.removeprefix('https://')
print(simple_url)

