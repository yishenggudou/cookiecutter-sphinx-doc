# -*- coding: utf-8 -*-

from sphinx.util.compat import Directive
from docutils import nodes

import os
import re
import popen2


class releasenotes(nodes.General, nodes.Element):
    pass

class ReleasenotesDirective(Directive):
    has_content = True
    option_spec = {
        'lang': unicode,
        'tag_only': int,
        'sur': unicode,
        'app': unicode
    }

    def run(self):
        print '[sphinxcontrib-releasenotes] args: %s' % self.options
        res = releasenotes('')
        if self.options.get('tag_only', 0) == 0:
            res['tag_only'] = False
        else:
            res['tag_only'] = True
        res['lang'] = self.options.get('lang', '')
        res['sur'] = self.options.get('sur', '')
        res['app'] = self.options.get('app', '')
        return [res]


def visit_html_releasenotes(self, node):
    env = self.builder.env
    for docname in env.found_docs:
        filename = docname

    git_command = 'git log --date=short --name-status --decorate=full'
    stdout, stdin, stderr = popen2.popen3(git_command)

    list = []
    commit = {}
    commit_log = ''
    for log in stdout:
        match = re.match('commit', log)
        if not match == None:
            commit['log'] = commit_log
            list.append(commit)
            commit = {}
            commit_log = ''

            commit['hash'] = log[match.end() + 1:match.end() + 8]

            commit['diff'] = ''
            git_command = 'git diff %s~..%s' % (commit['hash'], commit['hash'])
            stdout, stdin, stderr = popen2.popen3(git_command)
            for log in stdout:
                commit['diff'] += log

            # match tag
            # 1. tag: refs/tags/TAG)
            # 2. tag: refs/tags/TAG, refs/xxx/xxx .. )
            r = re.compile('tag: refs\/tags\/(.*)\)')
            tag = r.search(log)
            if tag == None:
                commit['tag'] = ''
            else:
                commit['tag'] = tag.group(1)

                # match tag2
                # 2. like a 1.
                r = re.compile('(.*),')
                tag = r.search(commit['tag'])
                if tag == None:
                    pass
                else:
                    commit['tag'] = tag.group(1)
        else:
            match = re.match('Author:', log)
            if not match == None:
                commit['author'] = log[match.end() + 1:]
                commit['survey'] = node['sur']
                commit['approval'] = node['app']
            else:
                match = re.match('Date:  ', log)
                if not match == None:
                    commit['date'] = log[match.end() + 1:]
                else:
                    if commit['tag'] == '' or node['tag_only'] == False:
                        commit_log += log
                    else:
                        git_command = 'git tag -v ' + commit['tag']
                        stdout, stdin, stderr = popen2.popen3(git_command)
                        for log in stdout:
                            commit_log = log

    commit['log'] = commit_log
    list.append(commit)
    del list[0]

    lang = self.builder.config.language
    lang_log = '- searched at conf.py DEFAULT en'
    if node['lang'] != '':
        lang = node['lang']
        lang_log = '- overwrite releasenotes directive :lang:'

    print '[sphinxcontrib-releasenotes] lang: %s %s' % (lang, lang_log)
    self.body += insert_release_note(list, node['tag_only'], lang)


def depart_releasenotes(self, node):
    pass


def setup(app):
    app.add_node(
        releasenotes, html=(visit_html_releasenotes, depart_releasenotes))

    app.add_directive('releasenotes', ReleasenotesDirective)

def insert_release_note(list, tag_only, lang):
    thead = {}
    if lang == 'ja':
        thead['headline'] = u'変更履歴'
        thead['revision'] = u'リビジョン'
        thead['date'] = u'日付'
        thead['commit_log'] = u'変更内容'
        thead['author'] = u'作成者'
        thead['survey'] = u'調査者'
        thead['approval'] = u'承認者'
    else:
        thead['headline'] = u'ReleaseNote'
        thead['revision'] = u'Revision'
        thead['date'] = u'Date'
        thead['commit_log'] = u'Commit log'
        thead['author'] = u'Author'
        thead['survey'] = u'Survey'
        thead['approval'] = u'Approval'

    js = '''
    <script type="text/javascript">
         $(function(){
              $("#releasenotes").on("click", 'p', function(){
                  var selector = ".releasenotes-diff-" + $(this).data("n");
                  $(selector).slideToggle("slow");
              });
         });
    </script>
    '''
    css = '''
    <style type="text/css">
        [class*="releasenotes-diff"] { display:none; }
    </style>
    '''

    html_content = []
    html_content.append(js)
    html_content.append(css)
    html_content.append('<div class="section" id="release_notes">')
    html_content.append('<h2>')
    html_content.append('%s' % thead['headline'])
    html_content.append(u'<a class="headerlink" href="#release_notes" title="Permalink to this headline">¶</a>')
    html_content.append('</h2>')
    html_content.append('<table border="1" id="releasenotes" class="docutils"><thead valign="bottom"><tr>')
    html_content.append(u'<th class="head">%s</th>' % thead['revision'])
    html_content.append(u'<th class="head">%s</th>' % thead['date'])
    html_content.append(u'<th class="head">%s</th>' % thead['commit_log'])
    html_content.append(u'<th class="head">%s</th>' % thead['author'])
    html_content.append(u'<th class="head">%s</th>' % thead['survey'])
    html_content.append(u'<th class="head">%s</th>' % thead['approval'])
    html_content.append('</tr></thead><tbody valign="top">')

    i = 0
    for l in list:
        i += 1
        if tag_only == True:
            if l['tag'] == '':
                pass
            else:
                html_content.append('<tr>')
                html_content.append('<td>%s</td>' % l['tag'].decode('utf-8'))
                html_content.append('<td>%s</td>' % l['date'].decode('utf-8'))

                html_content.append('<td>')
                html_content.append('<pre>%s</pre>' % l['log'].decode('utf-8'))
                html_content.append('<p data-n="%s">diff</p>' % i)
                html_content.append('<div class="releasenotes-diff-%s">' % i)
                try:
                    html_content.append('<pre>%s</pre>' % l['diff'].decode('utf-8'))
                except UnicodeDecodeError:
                    html_content.append('<pre>UnicodeDecodeError %s</pre>' % i)
                html_content.append('</div>')
                html_content.append('</td>')

                html_content.append('<td>%s</td>' % l['author'].decode('utf-8'))
                html_content.append('<td>%s</td>' % l['survey'])
                html_content.append('<td>%s</td>' % l['approval'])
                html_content.append('</tr>')
        else:
            html_content.append('<tr>')
            html_content.append('<td>%s</td>' % l['hash'].decode('utf-8'))
            html_content.append('<td>%s</td>' % l['date'].decode('utf-8'))

            html_content.append('<td>')
            html_content.append('<pre>%s</pre>' % l['log'].decode('utf-8'))
            html_content.append('<p data-n="%s">[show diff]</p>' % i)
            html_content.append('<div class="releasenotes-diff-%s">' % i)
            try:
                html_content.append('<pre>%s</pre>' % l['diff'].decode('utf-8'))
            except UnicodeDecodeError:
                html_content.append('<pre>UnicodeDecodeError %s</pre>' % i)
            html_content.append('</div>')
            html_content.append('</td>')

            html_content.append('<td>%s</td>' % l['author'].decode('utf-8'))
            html_content.append('<td>%s</td>' % l['survey'])
            html_content.append('<td>%s</td>' % l['approval'])
            html_content.append('</tr>')
    html_content.append('</tbody></table>')
    html_content.append('</div>')

    return html_content
