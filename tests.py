from converter import smartify

sentences = [
    "Liverpool, where there are currently 600 cases per 100,000 people, is expected to be placed under the most severe set of restrictions, with all the city's pubs forced to close",
    "In response to the criticism from some mayors of the scheme, a government spokesman said: Ministers are continuing to work closely with local leaders on how we can combat coronavirus together.",
    "Under the new restrictions, expected to be detailed by the prime minister in a statement to MPs on Monday, pubs and restaurants could be closed in areas where some of the highest numbers of cases are occurring and a ban on overnight stays is also being considered.",
    "We're now in a position where we don't know what's going to happen. Hospitality and everyone in hospitality has already went through the first wave of not being able to work and now we're coming into a second wave of it.",
    "Conda is a powerful package manager and environment manager that you use with command line commands at the Anaconda Prompt for Windows",
    "At SAS we envision a world where everyone can make better decisions, grounded in trusted data and assisted by the power and scale of SAS Analytics. When decisions happen at just the right moment, advancements are set in motion and the world moves forward."
]

# smartify where it's needed most...
trump = [
    "Crazy Nancy Pelosi is looking at the 25th Amendment in order to replace Joe Biden with Kamala Harris. The Dems want that to happen fast because Sleepy Joe is out of it",
    "Governor Whitmer of Michigan has done a terrible job. She locked down her state for everyone, except her husband’s boating activities. The Federal Government provided tremendous help to the Great People of Michigan.",
    "I do not tolerate ANY extreme violence. Defending ALL Americans, even those who oppose and attack me, is what I will always do as your President! Governor Whitmer—open up your state, open up your schools, and open up your churches"
]

sentences += trump

for s in sentences:
    print(smartify(s), end="\n---\n")