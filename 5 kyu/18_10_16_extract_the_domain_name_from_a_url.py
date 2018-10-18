# Write a function that when given a URL as a string,
# parses out just the domain name and returns it
# as a string. For example:
#
# domain_name("http://github.com/carbonfive/raygun") == "github"
# domain_name("http://www.zombie-bites.com") == "zombie-bites"
# domain_name("https://www.cnet.com") == "cnet"


def domain_name(url):
    possible_starts = ["https://www.", "http://www.", "https://", "http://", 'www.']

    for x in possible_starts:
        if url.startswith(x):
            url = url.replace(x, '')

    new_url = ""
    counter = 0
    while url[counter] != '.':
        new_url += url[counter]
        counter += 1

    return new_url


print(domain_name("http://github.com/carbonfive/raygun"), "github")
print(domain_name("http://www.zombie-bites.com"), "zombie-bites")
print(domain_name("https://www.cnet.com"), "cnet")
