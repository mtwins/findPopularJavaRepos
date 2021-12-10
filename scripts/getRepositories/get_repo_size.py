import csv
from time import sleep

from bs4 import BeautifulSoup
import requests


finalized_repos = [
    ("pytorch","serve"),
    ("alibaba","spring-cloud-alibaba"),
    ("LMAX-Exchange","disruptor"),
    ("open-telemetry","opentelemetry-java-instrumentation"),
    ("airbytehq","airbyte"),
    ("apache","incubator-doris"),
    ("TeamNewPipe","NewPipe"),
    ("testcontainers","testcontainers-java"),
    ("redis","jedis"),
    ("skylot","jadx"),
    ("Netflix","conductor"),
    ("apache","calcite"),
    ("OpenFeign","feign"),
    ("baomidou","mybatis-plus"),
    ("grpc","grpc-java"),
    ("azkaban","azkaban"),
    ("airbnb","lottie-android"),
    ("ReactiveX","RxAndroid"),
    ("crossoverJie","JCSprout"),
    ("json-path","JsonPath"),
    ("square","moshi"),
    ("termux","termux-app"),
    ("Netflix","zuul"),
    ("square","picasso"),
    ("pagehelper","Mybatis-PageHelper"),
    ("square","retrofit"),
    ("Tencent","tinker"),
    ("greenrobot","greenDAO"),
    ("resilience4j","resilience4j"),
    ("zhoutaoo","SpringCloud"),
    ("wildfirechat","server"),
    ("Netflix","eureka"),
    ("google","auto"),
    ("iBotPeaches","Apktool"),
    ("PhilJay","MPAndroidChart"),
    ("mapstruct","mapstruct"),
    ("clojure","clojure"),
    ("yidongnan","grpc-spring-boot-starter"),
    ("signalapp","Signal-Android"),
    ("JSQLParser","JSqlParser"),
    ("apache","incubator-shenyu"),
    ("spring-projects","spring-petclinic"),
    ("LuckSiege","PictureSelector"),
    ("alibaba","arthas"),
    ("apache","iceberg"),
    ("zo0r","react-native-push-notification"),
    ("linkedin","datahub"),
    ("apache","zeppelin"),
    ("Tencent","QMUI_Android"),
    ("dropwizard","metrics"),
    ("AsyncHttpClient","async-http-client"),
    ("alibaba","canal"),
    ("Qihoo360","RePlugin"),
    ("sshahine","JFoenix"),
    ("xuxueli","xxl-job"),
    ("asLody","VirtualApp"),
    ("dromara","hutool"),
    ("apache","shardingsphere-elasticjob"),
    ("apolloconfig","apollo"),
    ("real-logic","aeron"),
    ("CymChad","BaseRecyclerViewAdapterHelper"),
    ("alibaba","druid"),
    ("square","javapoet"),
    ("react-native-image-picker","react-native-image-picker"),
    ("koral--","android-gif-drawable"),
    ("pxb1988","dex2jar"),
    ("cryptomator","cryptomator"),
    ("Tencent","APIJSON"),
    ("PaperMC","Paper"),
    ("LawnchairLauncher","lawnchair"),
    ("PojavLauncherTeam","PojavLauncher"),
    ("exadel-inc","CompreFace"),
    ("freyacodes","Lavalink"),
    ("android-hacker","VirtualXposed"),
    ("bumptech","glide"),
    ("linlinjava","litemall"),
    ("huanghongxun","HMCL"),
    ("alibaba","easyexcel"),
    ("gedoor","MyBookshelf"),
    ("halo-dev","halo"),
    ("jeecgboot","jeecg-boot"),
    ("macrozheng","mall"),
    ("facebook","fresco"),
    ("metersphere","metersphere"),
    ("kiwibrowser","src.next"),
    ("LSPosed","LSPosed"),
    ("M66B","NetGuard"),
    ("questdb","questdb"),
    ("wiremock","wiremock"),
    ("eclipse-vertx","vert.x"),
    ("knowm","XChange"),
    ("redisson","redisson"),
    ("quarkusio","quarkus"),
    ("strimzi","strimzi-kafka-operator"),
    ("ElderDrivers","EdXposed"),
    ("rubenlagus","TelegramBots"),
    ("traccar","traccar"),
    ("andOTP","andOTP"),
    ("xuexiangjys","XUI"),
    ("tarunsinghofficial","HacktoberFest")
]



def get_repo_info():
    page = requests.get(repo['html_url'])
    soup = BeautifulSoup(page.content, 'html.parser')
    try:
        commit_elements = soup.find_all('span', class_="d-none d-sm-inline")
        commits = commit_elements[1].getText().split()[0]
    except IndexError:
        commits = "0"  # if coud not find commits set as 0 for now- have to manually find them

    license = "None"
    if repo['license']:
        license = repo['license']['name']
    writer.writerow(
        [repo['name'], repo['html_url'], repo['stargazers_count'], repo['forks_count'], int(commits.replace(",", "")),
         license, repo['updated_at'], repo['size'], repo['visibility']])


if __name__ == '__main__':
    with open('repository-size.csv', mode='w') as result_file:
        writer = csv.writer(result_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow( ["name", "size"])
        largest_size=0
        largest_repo=""
        for repo_number in range(0,100):
            response = requests.get(
                f'https://api.github.com/repos/{finalized_repos[repo_number][0]}/{finalized_repos[repo_number][1]}', headers={'Authorization': 'token {replace with personal access token}'})
            sleep(1)
            # print(response.json())
            try:
                print(f'{finalized_repos[repo_number][0]}/{finalized_repos[repo_number][1]}: {response.json()["size"]} kb')
                if(response.json()["size"]>largest_size):
                    largest_size=response.json()["size"]
                    largest_repo=f'{finalized_repos[repo_number][0]}/{finalized_repos[repo_number][1]}'

                writer.writerow([finalized_repos[repo_number][1], response.json()["size"]])
            except:
                print(f'Could not find size for {finalized_repos[repo_number][0]}/{finalized_repos[repo_number][1]}')
                writer.writerow([finalized_repos[repo_number][1], '0 mb'])

            print(f'The largest repo is {largest_repo}, the largest size is: {largest_size} ')

