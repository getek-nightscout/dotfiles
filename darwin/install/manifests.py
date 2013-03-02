# -*- coding: utf-8 -*-
#!/usr/bin/env python

#pylint: disable=C0103, W0702
"""
Example manifest:

manifests.append({
    'name' : 'configobj',
    'check' : '/Library/Python/2.7/site-packages/configobj.py',
    'force' : True,
    'install' : 'sudo pip install configobj',
})
"""

manifests = []

#install ruby and add dupes, versions repos
manifests.append({
    'name' : 'brew',
    'install' : 'ruby -e "$(curl -fsSkL raw.github.com/mxcl/homebrew/go)"',
})

manifests.append({
    'name' : 'homebrew/versions',
    'check' : '/usr/local/Library/Taps/homebrew-versions',
    'install' : 'brew tap homebrew/versions',
})

manifests.append({
    'name' : 'homebrew/versions',
    'check' : '/usr/local/Library/Taps/homebrew-versions',
    'install' : 'brew tap homebrew/dupes',
})


#bash stuff
manifests.append({
    'name' : 'bash',
    'check' : '/usr/local/bin/bash',
    'install' : 'brew install bash',
})

manifests.append({
    'name' : 'bash-completion2',
    'check' : '/usr/local/share/bash-completion/bash_completion',
    'install' : 'brew install bash-completion2'
})


#git stuff
manifests.append({
    'name' : 'git',
    'install' : 'brew install git'
})

manifests.append({
    'name' : 'git-extras',
    'install' : 'brew install git-extras'
})


#node stuff
manifests.append({
    'name' : 'node',
    'install' : 'brew install node'
})

manifests.append({
    'name' : 'jshint',
    'check' : '/usr/local/share/npm/bin/jshint',
    'install' : 'npm install jshint'
})


#ruby stuff
manifests.append({
    'name' : 'rbenv',
    'install' : 'brew install rbenv'
})

manifests.append({
    'name' : 'ruby-build',
    'install' : 'brew install ruby-build'
})


#other stuff
manifests.append({
    'name' : 'htop',
    'install' : 'brew install htop-osx'
})

manifests.append({
    'name' : 'mosh',
    'install' : 'brew install mosh'
})

manifests.append({
    'name' : 'ack',
    'install' : 'brew install ack'
})

manifests.append({
    'name' : 'nano',
    'check' : '/usr/local/bin/nano',
    'install' : 'brew install nano',
})