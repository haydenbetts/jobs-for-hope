import RAKE

def main():

    # read in sample job skills entry
    with open('SampleJobSkills.txt', 'r') as myfile:
        data=myfile.read().replace('\n', ' ')

    # initialize RAKE https://github.com/fabianvf/python-rake
    # using a built-in list of stopwords
    Rake = RAKE.Rake(RAKE.SmartStopList())
    rake_results = Rake.run(data)
    
    # return array of top keywords
    return_top_keywords(rake_results, 5)

def return_top_keywords(rake_results, num_keywords):
    keywords = []

    for i in range(num_keywords):     
        keywords.append((rake_results[i][0]))
        i += 1

    return keywords


if __name__ == "__main__":
    main()


