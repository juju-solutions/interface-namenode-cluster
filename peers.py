# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from charms.reactive import RelationBase
from charms.reactive import hook
from charms.reactive import scopes

from charmhelpers.core import hookenv

from jujubigdata import utils


class NameNodePeers(RelationBase):
    scope = scopes.UNIT

    @hook('{relation_name}.relation-joined')
    def joined(self):
        conv = self.conversation()
        conv.set_state('{relation_name}.joined')

    @hook('{relation_name}.relation-departed')
    def departed(self):
        conv = self.conversation()
        conv.remove_state('{relation_name}.joined')

    def nodes(self):
        node_names = [hookenv.local_unit().replace('/', '-')]
        for conv in self.conversations():
            node_names.append(conv.scope.replace('/', '-'))
        return sorted(node_names)[:2]  # only use the first two peers, if more

    def hosts_map(self):
        result = {}
        for conv in self.conversations():
            ip = utils.resolve_private_address(conv.get_remote('private-address', ''))
            host_name = conv.scope.replace('/', '-')
            result.update({ip: host_name})
        return result