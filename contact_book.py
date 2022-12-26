{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "0e7ed88c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The Contact Book\n"
     ]
    }
   ],
   "source": [
    "print(\"The Contact Book\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "33e9b6e6",
   "metadata": {},
   "outputs": [],
   "source": [
    "names = []\n",
    "phone_numbers = []\n",
    "email_ids = []\n",
    "max = 3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "de50e82a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Name :  Poonam\n",
      "Phone Number : 7678320925\n",
      "Email-Id: biswaspoonam002@gmail.com\n",
      "Name :  Pushpa\n",
      "Phone Number : 9873839886\n",
      "Email-Id: -\n",
      "Name :  Archana\n",
      "Phone Number : 9873579328\n",
      "Email-Id: archanabiswas147@gmail.com\n"
     ]
    }
   ],
   "source": [
    "for i in range(max):\n",
    "    name = str(input(\"Name :  \"))\n",
    "    phone_number = int(input(\"Phone Number : \"))\n",
    "    email_id = str(input(\"Email-Id: \"))\n",
    "    names.append(name)\n",
    "    phone_numbers.append(phone_number)\n",
    "    email_ids.append(email_id)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "53149130",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Poonam\t\t\t7678320925\n",
      "Pushpa\t\t\t9873839886\n",
      "Archana\t\t\t9873579328\n",
      "\n",
      "Enter search term: Pushpa\n",
      "Search result:\n",
      "Name: Pushpa, Phone Number: 9873839886, Email-Id: -\n"
     ]
    }
   ],
   "source": [
    "for i in range(max):\n",
    "    print(\"{}\\t\\t\\t{}\".format(names[i], phone_numbers[i], email_ids[i]))\n",
    "\n",
    "search_term = input(\"\\nEnter search term: \")\n",
    "\n",
    "print(\"Search result:\")\n",
    "if search_term in names:\n",
    "    index = names.index(search_term)\n",
    "    phone_number = phone_numbers[index]\n",
    "    email_id = email_ids[index]\n",
    "    print(\"Name: {}, Phone Number: {}, Email-Id: {}\".format(search_term, phone_number, email_id))\n",
    "\n",
    "else:\n",
    "    print(\"Name Not Found\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "288ddc24",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
