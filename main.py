def calculator(a, operator, b):
	"""Ikki son ustida arifmetik amal bajaradi."""
	if operator == "+":
		return a + b
	if operator == "-":
		return a - b
	if operator == "*":
		return a * b
	if operator == "/":
		if b == 0:
			raise ZeroDivisionError("Nolga bo'lish mumkin emas")
		return a / b
	if operator == "**":
		return a ** b
	if operator == "%":
		if b == 0:
			raise ZeroDivisionError("Nolga bo'lish mumkin emas")
		return a % b
	raise ValueError(f"Noma'lum amal: {operator}")


def read_number(prompt):
	"""Foydalanuvchidan son so'raydi, xato kiritilsa qayta so'raydi."""
	while True:
		text = input(prompt)
		try:
			return float(text)
		except ValueError:
			print("Iltimos, to'g'ri son kiriting.")


def main():
	print("=== Kalkulyator ===")
	print("Amallar: +  -  *  /  **  %")
	print("Chiqish uchun amal o'rniga 'q' yozing.\n")

	while True:
		a = read_number("Birinchi son: ")
		operator = input("Amal: ").strip()
		if operator.lower() == "q":
			print("Xayr!")
			break
		b = read_number("Ikkinchi son: ")

		try:
			result = calculator(a, operator, b)
		except (ZeroDivisionError, ValueError) as error:
			print(f"Xato: {error}\n")
			continue

		if result == int(result):
			result = int(result)
		print(f"Natija: {a:g} {operator} {b:g} = {result}\n")


if __name__ == "__main__":
	main()
