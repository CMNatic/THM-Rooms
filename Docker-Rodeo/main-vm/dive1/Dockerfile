FROM debian:buster-slim

RUN mkdir -p /home/user
RUN touch "/home/user/flag.txt"

RUN apt-get update -y

RUN echo "Apt updated"

RUN echo "not this layer" > /home/user/flag.txt

# Lets put this user add on another layer for clarity
RUN useradd -m user -s /bin/bash && \
  mkdir -p /home/user/.ssh && \
  echo "user:user" | chpasswd && \
  echo "user successfully added"

RUN echo "thm{the_final_layer}" > /home/user/flag.txt