# GitBackdorizer (BETA)
GitBackdorizer is a proof of concept, fully inspired in Ulisses Castro's [50 ton of backdoors](https://www.slideshare.net/ulissescastro/50-ton-of-backdoors) talk, that abuses the lack of user attention to steal git access credentials.

## How it Works
#### Dropper
The dropper is designed to have the highest possible compatibility, avoiding any non-sh specific feature. It works by:
- Identify if the backdorized git hook is the pre-push hook or any other
- Drop the backdoor payload to the specific hook
- Give execution permission

#### Payload
Payloads are also designed to have the highest possible compatibility avoiding non-sh features.There are currently two types of payload, the generic and the pre-push specific.

The **generic** payload tries to identify the remote type (HTTPS/SSH) by:
- Checking the current branch: `git branch --contains HEAD`
- Collecting the remote name of the branch (through git config)
- Collecting the remote url of the remote name (through git config)
Then it will check if url is https or ssh.

The **pre-push** payload will check directly the provided git information for the url (second hook parameter for pre-push).

## Demo
How to use gitbackdorizer to exploit user confidence and steal their credentials:

[![GitBackdorizer - stealing credentials](https://img.youtube.com/vi/ka8uJqaDYOs/0.jpg)](https://www.youtube.com/watch?v=ka8uJqaDYOs)

## Greetz
- [Ulisses Castro](https://github.com/ulissescastro) - 50 ton of backdoors (https://www.slideshare.net/ulissescastro/50-ton-of-backdoors)
- [Giovani Silva](https://github.com/giovanifss/) - Wrote Infection Shell Script
