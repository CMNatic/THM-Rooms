
# THM-Rooms

Repo for my OSS'd TryHackMe rooms


# [OWASP10-A8-Insecure-Deserialization](https://github.com/CMNatic/THM-Rooms/tree/master/OWASP10-A8-Insecure-Deserialization)

Built for [TryHackMe's OWASP10 event](https://tryhackme.com/room/owasp10), this *Vim Vs. Nano* themed room highlights how data is serialised and respectively deserialised and how it can be exploited.


### Features ✨
- Plaintext and base64 encoded cookie flags
- RCE (with [rce.py](https://github.com/CMNatic/THM-Rooms/blob/master/OWASP10-A8-Insecure-Deserialization/rce.py)) via python pickles
- Quiz "bonus flag" made possible by the kind [contributors at UrbanInstitute for creating the framework for this quiz.](https://github.com/UrbanInstitute/quick-quiz)

### To-Do :pencil:
- Publish DockerHub Image

### Installation
- Deployable with flask server, Dockerfile or behind wsgi & reverse proxy i.e. Nginx
- Support not provided

![enter image description here](https://img.shields.io/badge/Supported-No-red)
![enter image description here](https://img.shields.io/github/languages/count/cmnatic/THM-Rooms)