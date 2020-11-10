FROM ubuntu:18.04

LABEL maintainer "@CMNatic <https://cmnatic.co.uk">

RUN apt-get -qq update && \
  DEBIAN_FRONTEND=noninteractive \
  apt-get -y --no-install-recommends -qq install \
  openssh-server \
  apt-utils \
  libcap2-bin \
  linux-headers-$(uname -r) \
  sudo \
  curl && \
  mkdir -p /var/run/sshd && \
  mkdir -p /root/.ssh && \
  echo "Packages installed"

# Lets put this user add on another layer for clarity
RUN useradd -m danny -s /bin/bash && \
  mkdir -p /home/danny/.ssh && \
  echo "danny:danny" | chpasswd && \
  echo "danny user successfully added"

# Add user to sudoers

RUN echo "danny ALL=(ALL,ALL) NOPASSWD: /bin/bash" >> /etc/sudoers && \
  echo "danny user added to sudoers"

WORKDIR /etc/ssh

# Take values from ARGS and modify sshd_config accordingly
RUN \
    echo "root:danny" | chpasswd && \
    echo "Successfully changed root password" && \
    \
    sed --in-place 's/^\(UsePAM\|UseDNS\)/#\1/' sshd_config && \
    echo "" >> sshd_config && \
    echo "UsePAM no" >> sshd_config && \
    echo "UseDNS no" >> sshd_config && \
    echo "PermitRootLogin yes" >> sshd_config && \
    echo "SSHD updated"

EXPOSE 22

CMD    ["/usr/sbin/sshd", "-D"]
