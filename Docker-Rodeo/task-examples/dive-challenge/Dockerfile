FROM ubuntu:18.04

LABEL maintainer "@CMNatic <https://cmnatic.co.uk">
LABEL description "CVE-2019-14287 Exploit built by CMNatic for UoG CTF & THM"

RUN apt-get -qq update && \
  DEBIAN_FRONTEND=noninteractive \
  apt-get -y --no-install-recommends -qq install \
  openssh-server \
  apt-utils \
  sudo=1.8.21p2-3ubuntu1 && \
  mkdir -p /var/run/sshd && \
  mkdir -p /root/.ssh && \
  echo "Packages installed"

# Lets create our first user add on another layer for clarity
RUN useradd -m uogctf -s /bin/bash && \
  mkdir -p /home/uogctf/.ssh && \
  echo "uogctf:uogctf" | chpasswd && \
  echo "uogctf user successfully added"
# Add user to sudoers

RUN echo "uogctf ALL=(ALL,!root) NOPASSWD: /bin/bash" >> /etc/sudoers && \
  echo "uogctf user added to sudoers"



WORKDIR /etc/ssh

# Take values from ARGS and modify sshd_config accordingly
RUN \
    echo "root:uogctf" | chpasswd && \
    echo "Successfully changed root password" && \
    \
    sed --in-place 's/^\(UsePAM\|UseDNS\)/#\1/' sshd_config && \
    echo "" >> sshd_config && \
    echo "UsePAM no" >> sshd_config && \
    echo "UseDNS no" >> sshd_config && \
  echo "SSHD updated"

EXPOSE 22

CMD    ["/usr/sbin/sshd", "-D"]