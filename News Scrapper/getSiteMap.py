from usp.tree import sitemap_tree_for_homepage


def show_URL(url,media):
    tree = sitemap_tree_for_homepage(url)


    # all_pages() returns an Iterator
    #for page in tree.all_pages():
        #print(page)


    tree_urls = [page.url for page in tree.all_pages()]

    print("give me the size",len(tree_urls))
    # Save the URLs to a TXT file
    output_file = f'data/sitemap_{media}.txt'
    with open(output_file, 'w') as f:
        f.write('\n'.join(tree_urls))

    print(f"Sitemap saved to {output_file}")


#Radio Canada
#show_URL("https://ici.radio-canada.ca/",'radio_canada')

#LaPresse
#show_URL("https://www.lapresse.ca/",'lapresse')

#Radio Canada Test
#show_URL("https://ici.radio-canada.ca/ottawa-gatineau",'radio_canada_ottawa-gatineau')


#Devoir
#show_URL("https://www.ledevoir.com/",'devoir')

#Journal de Montreal
#show_URL("https://www.journaldemontreal.com/",'Journal_de_Montreal')


#Gazette
#show_URL("https://montrealgazette.com/robots.txt",'gazette')


#https://ici.radio-canada.ca/abitibi-temiscamingue

#Gazette
#show_URL("https://ici.radio-canada.ca/abitibi-temiscamingue",'radio_Canada_abitibi_temiscamingue')

#Radio canda
#show_URL("https://ici.radio-canada.ca/environnement",'radio_canada_env')


#CBC

#show_URL("https://www.cbc.ca/",'cbc')


show_URL("https://www.journaldemontreal.com/rss.xml",'rss_test')