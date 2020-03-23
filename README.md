![Vue](https://github.com/Stack-Box/StackBox/workflows/Vue/badge.svg) ![Flask](https://github.com/Stack-Box/StackBox/workflows/Flask/badge.svg) [![Slack](https://img.shields.io/badge/slack-@stackboxworkspace-purple.svg?logo=slack
)](https://stackboxworkspace.slack.com/)

# StackBox
> Wiki is a good place to start!

Stackbox helps you create app stacks loaded with all your favourite clients, services and infra in under 5 mins. The aim of the project is to help developers setup quick infra and boilerplates to start the dev work asap. Ideally this project is to help rapid prototyping, building PoCs or writing code for hackathons.

1. [**About**](https://github.com/Stack-Box/StackBox/wiki)
2. [**Get Started**](https://github.com/Stack-Box/StackBox/wiki/Get-started)
3. [**Working**](https://github.com/Stack-Box/StackBox/wiki/Working)
4. [**Debugging**](https://github.com/Stack-Box/StackBox/wiki/Debugging)

# Get Started
## Run

`sh stack_box.sh <client-1> <client-2> <service-1> <service-2>`

Jump to [_**example-stacks**_](https://github.com/Stack-Box/StackBox/blob/master/README.md#example-stacks) to quickly try a run

## Support
### Supported Clients

- vue
- flask

### Supported Services

- mysql
- elasticsearch
- kibana
- nginx
- kafka (BROKEN!! - https://github.com/Stack-Box/StackBox/issues/21)
- zookeper

## Example Stacks

The following is a list of example stacks you could spin-up using Stackbox and quickly get-started with your development.

### 1. Flask-Vue-Mysql-Elasticsearch
#### Run

`sh stack_box.sh flask vue mysql elasticsearch`

#### Test
After the run is finished, the final log should look like the one below.

```
flask is up at http://localhost:80
vue is up at http://localhost:8080
elasticsearch is up at http://localhost:9200
mysql is up at http://localhost:3306
```

Now you can visit http://localhost:8080 to view the Vue frontend. From there you can click on Mysql/Elasticsearch links to view the preloaded data from mysql/elasticsearch containers being rendered.

**Visit [Working](https://github.com/Stack-Box/StackBox/wiki/Working) or [Debugging](https://github.com/Stack-Box/StackBox/wiki/Debugging)  pages to know more about internal details.**

## To be added Services and Clients

📢 **Contributors needed!!** 📢

**Aux Services**
- [ ] Dynamo
- [ ] S3
- [ ] Postgres
- [ ] CouchDB
- [ ] MongoDB
- [x] Kafka
- [ ] Hadoop
- [ ] Clients

**Frontend clients**
- [ ] Angular
- [ ] React

**Backend services**
- [ ] Rails
- [ ] Django
- [ ] Springboot
- [ ] Golang
