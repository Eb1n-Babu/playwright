from  infopark_jobs import info_park_jobs

if __name__ == '__main__':
    search_keyword = input("Enter job keyword to search: ").strip()
    try:
        info_park_jobs(search_keyword)
    except TypeError:
        print("Sorry, job search failed")
    except ValueError:
        print("Sorry, job search failed")
    finally:
        print("Job search successful")
