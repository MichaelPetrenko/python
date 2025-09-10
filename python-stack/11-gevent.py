# pip install gevent
import gevent

def parser(site_name):
    gevent.sleep(2)
    print(site_name)

if __name__ == '__main__':
    jobs = [
        gevent.spawn(parser, site) for site in ["site1", "site2", "site3"]
    ]
    gevent.wait(jobs)

    gevent.joinall([gevent.spawn(parser, site) for site in ["site1", "site2", "site3"]])