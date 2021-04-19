# Given a valid (IPv4) IP address,
# return a defanged version of that IP address.

# A defanged IP address replaces every period "." with "[.]".

def defangIPaddr(address: str) -> str:
    return address.replace('.', '[.]')


ipAddress = '1.2.3.4'
print(defangIPaddr(ipAddress))
