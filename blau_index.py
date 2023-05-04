from pymongo import MongoClient


class BlauIndex:

    def __init__(self):
        self.projects = [
            {"owner": "google", "repo": "ExoPlayer"},
            {"owner": "google", "repo": "guava"},
            {"owner": "google", "repo": "gson"},
            {"owner": "google", "repo": "dagger"},
            {"owner": "google", "repo": "guice"},
            {"owner": "spring-projects", "repo": "spring-boot"},
            {"owner": "spring-projects", "repo": "spring-security"},
            {"owner": "Netflix", "repo": "zuul"},
            {"owner": "Netflix",  "repo": "eureka"},
            {"owner": "Netflix", "repo": "Hystrix"},
            {"owner": "Netflix", "repo": "conductor"}
        ]
        self.mongo_connection = MongoClient("mongodb://localhost:27017/")

    def calc_blau_index(self):

        for project in self.projects:
            project_name = project['repo']
            project_owner = project['owner']

            database = self.mongo_connection[project_owner + '-' + project_name]

            metrics = list(database['metrics'].find({}))

            has_gender = {'gender': list(), 'count': list()}
            for metric in metrics:

                if 'number_males' in metric.keys():
                    has_gender['gender'].append('male')
                    has_gender['count'].append(metric['number_males'])
                    has_gender['gender'].append('female')
                    has_gender['count'].append(metric['number_females'])


            gender = pd.DataFrame(has_gender)
            gender = gender.groupby('gender')['count'].apply(self.blaus_index).reset_index(name='Gender Diversity')

            print(project_name)
            print(gender)


    def blaus_index(self, arr):
        return 1 - sum((arr.value_counts() / len(arr)) ** 2)