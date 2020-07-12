import requests

def main ():
        
        url='https://engine.scicrop.com/scicrop-engine-web/api/v1/jobs/post_resume'

        newHeaders = {'Content-type': 'application/json'}

        curriculo={
                  'full_name': 'Carolina Tack Trujillo',
                  'email': 'tack.carol.fly@live.com',
                  'mobile_phone': '+55 (11) 99205-9685',
                  'age': 28,
                  'home_address': 'Av. Henriqueta Mendes Guerra, 1330',
                  'start_date': 1594562400,
                  'opportunity_tag': 'dev_intern_200',
                  'past_jobs_experience': 'I worked as laboratory analyst, foccused in data analytics and development of healthcare strategies and systems.',
                  'degrees': [
                    {
                      'institution_name': 'UNIP - University Paulista',
                      'degree_name': 'System Analysis and Development',
                      'begin_date': 1583049600,
                      'end_date': 1638396000
                    },
                    {
                      'institution_name': 'UNIFESP - Federal University of São Paulo',
                      'degree_name': 'Biochemical Pharmacy',
                      'begin_date': 1425196800,
                      'end_date': 1642024800
                    },
                    {
                      'institution_name': 'UNASP - Adventist Center University',
                      'degree_name': 'Highschool - Exact Science',
                      'begin_date': 1170316800,
                      'end_date': 1259704800
                    }
                  ],
                  'programming_skills': [
                    'python',
                    'java',
                    'VBA',
                    'HTML',
                    'CSS'
                  ],
                  'database_skills': [
                    'mysql',
                    'postgresql',
                    'oracle'
                  ],
                  'hobbies': [
                    'Hangout with friends',
                    'Whatching commedy series',
                    'Play with my cats'
                  ],
                  'why': 'During my actual job, i realize that i have much more affinity with technological area than healthcare.',
                  'git_url_repositories': 'https://github.com/tackcarol'
                }
        
        res = requests.post(url, json=curriculo, headers=newHeaders)

        print("Status code: ", res.status_code)
        print("Printing Entire Post Request")
        print(res.json())

if __name__ == '__main__':
	main()
