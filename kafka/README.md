# Kafka

Hands-on Apache Kafka material: shell scripts and configs from two
courses — Kafka basics (CLI, topics, consumer groups) and Kafka Connect
(sources & sinks).

## kafka_course1/ — Kafka basics

Companion scripts for *Apache Kafka Series: Learn Apache Kafka for
Beginners* by Stéphane Maarek (course:
<https://www.udemy.com/course/apache-kafka/>, companion repo:
<https://github.com/simplesteph/kafka-beginners-course>).

| Folder | What it does |
|---|---|
| `0-start-kafka/` | Download & start Kafka (binaries) on Linux, macOS, or Windows |
| `1-kafka-cli/` | CLI walkthrough: topics, console producer/consumer, consumer groups, resetting offsets |
| `2-kafka-topic-configurations/` | Topic config + log compaction |
| `annex-1-start-kafka/` | Alternate ways to start Kafka: Confluent CLI, multi-broker binaries, Docker, remote VM |

### How to work through it

1. Pick your platform in `0-start-kafka/` and follow the setup + start
   scripts (they download Kafka from <https://kafka.apache.org/downloads>;
   requires Java 8+).
2. Work through `1-kafka-cli/` in order (0 → 5), then
   `2-kafka-topic-configurations/`.
3. `annex-1-start-kafka/` is optional — pick the start method you prefer.

## kafka_course2/ — Kafka Connect

Scripts & configs from the Kafka Connect workshop
(<https://github.com/rvanrijn/workshop-apache-kafka-connect>) —
`source/` demos (file stream, twitter source), `sink/` demos
(Elasticsearch, Postgres, REST API), plus a two-worker distributed
Connect setup under `setup/`.

### How to work through it

Requires Docker. Start the stack from this directory:

```sh
# sources
docker-compose up kafka-cluster

# sinks (adds Elasticsearch + Postgres)
docker-compose up kafka-cluster elasticsearch postgres
```

Then follow `kafka-connect-tutorial-sources.sh` and
`kafka-connect-tutorial-sinks.sh` (or run the individual demo scripts in
`source/` and `sink/`). `setup/setup.sh` walks through configuring a
second distributed Connect worker against a real Kafka install
(≥ 0.11.0.1).

Note: the docker-compose pins old images (`itzg/elasticsearch:2.4.3`,
`postgres:9.5-alpine`, untagged `landoop/fast-data-dev`); expect to
update image tags if a base image has been removed from the registry or
is too old for your platform.
