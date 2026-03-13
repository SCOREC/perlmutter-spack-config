# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack.package import *

RELEASES = [
{
    'version': '2025.1-250602dev',
    'components': {
       'msadv': ['328470278ddb0b48b4d826214486e397acf5044550ab86353924c26105a8ae78', 'adv'],
       'fdcore': ['cab00247a75ad7ca9a0f6f7b997e58ebef3957310bfb5430139a581ea2d9e365', 'base'],
       'mscore': ['e2224541a1610ef500a8c8f88e7f34bff70dca050cb24b1e5e5a0659e60f34f1', 'base'],
       'msparallelmesh': ['5c91515ae2be78c07a7d01e8a388853ef63ea58bbd4e9804a0b8fb43fe98c921', 'parallelmesh'],
       'octree': ['d38aaa55c1c62b0b9894c65f1ed5914be2476d6cc82f488abf608559175374e4', 'octree'],
       'mscrack': ['df32f9fcb68696ee32ac1fd6071749fd713b59cfd0f5b1f25d71922e3436582e', 'crack'],
       'discrete': ['b594a03e87e58093c6b0638dbf871418414db2191a211cfb3d62b95fa5da1768', 'discrete'],
       'opencascade': ['c94f2cbdfe1ec8dd55b7fbd6c83d19e1f15e11d5b22e23d2a5a93aa52b2cccb2', 'opencascade'],
       'aciskrnl': ['c36a2f9569e9b47c381853e87b9b5b7ca0c67fbd94d213d2253ba24f58577e6f', 'acis'],
       'gmadv': ['68841f4b1103f35eed88789c361106bd0fc76f981f1cfa12a5540e9a5067b9cf', 'advmodel'],
       'msparalleladapt': ['898c7a5f59460236a63b961ca612a434d3e7ca690a090cf14416bb4aa6113ab0', 'paralleladapt'],
       'pskrnl': ['2c563c4ffc78f7eff6c54f3cb1faedf47a09b0ae542edaff977f35a4d121176a', 'parasolid'],
       'discretemodeling': ['91bbe6056467c0d709ce3708f33adc2d30434a2d6a7115f4687cda87a9814e5c', 'discrete'],
       'gmcore': ['87a7da85d866ec82a4667d349df9192123466fd5651c05f66bd73a31e70811c3', 'base'],
       'msadapt': ['93f18e261454fe9e250a0e41a1afa4d14d2dac037a0f6206bbd328c149f2b7e0', 'base'],
       'gmvoxel': ['cf2a1c63b486a9085012d0a25d3828cd816f4ff6b0494507a61905db224e8258', 'voxel'],
       'gmabstract': ['cfce1e6834c4ec072b95efc5f833b584dfa6c801841657aa2fa915faf6c2240a', 'abstract'],
    },
    'docs': {
       'GeomSimDiscrete': ['f522769a79eb10633188091441add0da1148b9f91881e7525c17c9dafffd7ff6', 'discrete'],
       'GeomSimAbstract': ['c5ec727f3fe4cdb6c3e91819d4eac137c3f3180e40886531950a9a9456f119ac', 'abstract'],
       'ParallelMeshSim': ['4489d0d0464fdb29e95433a84cba4b45d3c7dc18bf8cedb5abfaa71f75daa78e', 'parallelmesh'],
       'ParallelMeshSimAdapt': ['f363d52310366135b134108da76d874b012f7e3a8451337ca6e826a379b4a501', 'paralleladapt'],
       'GeomSim': ['b95ca1ec56c9e6ad185dbdce5fe9817d726a945cb9091ccb10e42a931407b3f6', 'base'],
       'MeshSimAdapt': ['b5f240ff77f5f8726f5fc363c3221d57a636079487ce6513bae8c1d0e1ffe8ad', 'base'],
       'MeshSimCrack': ['76b8c1eaf1f9132f1726ad5324ab944cb2c2258a939add451292f3457729160b', 'crack'],
       'GeomSimDiscreteModeling': ['83b963a1dabb2719a9a2040576657163c960b50da3b516514b3f56c8619835d6', 'discrete'],
       'MeshSimAdvanced': ['b6086ec2e52b1862e34077f67aaa7d401a76c1a9f9915f44f4b3629c0b06c550', 'adv'],
       'GeomSimParasolid': ['82f3bc7474a0a412efd021cfb5a5d42182f39f3469bb610c640c5beeac6886e5', 'parasolid'],
       'MeshSim': ['3dbd693838c072cc1231946433b342ef3e9d5e1f6986d3fcc0d7bbd98d5fd0b8', 'base'],
       'GeomSimGranite': ['2770b1e6eb5a50fc588e130e281470e1bf312521f22a722fa5e350a322b5e965', 'granite'],
       'GeomSimOpenCascade': ['3231cf7d93cfd0715f34befabd5ba8287e2ade4dd7307e32d8101007041e6619', 'opencascade'],
       'GeomSimAdvanced': ['00eeb5425a551dc9b3d645da9954e811b3f47688ac2878ea70f5125b480d4fcb', 'advmodel'],
       'GeomSimVoxel': ['8952468d98bd1000dcb3c0c6e02d7c33b057828801ee98ba879aa91d7c22bf97', 'voxel'],
       'MeshSimOctree': ['8b94bab905d3048be31ee37e6ea64aea96d6d71937054c3134eeb8a05827d8b8', 'octree'],
       'GeomSimAcis': ['247224890f1ab5e5cf674f9e5d2727327630c9a57be293f34aceabc62610fb05', 'acis'],
       'FieldSim': ['e85f98a298b464815be7257531162f4cc62b9f629562c7378fe764024bc49c92', 'base'],
    }
},
{
    'version': '2025.1-250507dev',
    'components': {
       'fdcore': ['bb0692fda460d862b89eade13f8801540d54e86055925df04dcb03eefb14a2ed', 'base'],
       'gmvoxel': ['d88c36521baca05475f05ad0e7cab3e514cc6430ee45b248b0c68e5378f1a2d1', 'voxel'],
       'msadapt': ['8af4821b7f7f5e20cd4b6d1381dc85c9fe8bd9624d6b91d4662a17208d7259d4', 'base'],
       'aciskrnl': ['2f46cc4d14c0ce0411fe81b69fa5973aa92a8423b658b8b087f4f263fc72a33a', 'acis'],
       'mscore': ['6b44d45c4bb42e2731945a6ae8ae8851b9b422bb33294c0ce23bfe32c23f5897', 'base'],
       'discrete': ['0d72d0998d2386a66763007f43d304b4367cb41b7f6255178a83548cd856671e', 'discrete'],
       'octree': ['47a2e3d5d9a7adc181076600d63b9a4fbc7770c232b5a3d436625560eb2bc835', 'octree'],
       'msparallelmesh': ['ab79660dcebd8d0880c325072cc9208525c3d6fca0f3b3fd90398eb36d580ac8', 'parallelmesh'],
       'gmabstract': ['26d7da88638a190641b6f9d833fbc29e8c8891473f9a8e23c6c45b721864e6bf', 'abstract'],
       'msparalleladapt': ['cc9cc23c67f86fce1e258940f4a54057e60026e4c889697250aed2616120645f', 'paralleladapt'],
       'msadv': ['7d8fb9fe1b782d9504c0c015103de45222d9c8545f989f10bde4808b1f1451ff', 'adv'],
       'opencascade': ['61e3801517c841b207ccc4a8c000f73dc8e9faf0501e928740e6613c1c029705', 'opencascade'],
       'mscrack': ['2d41c60106368b2f6eb0f662ca4c43a4ac6f188b9796fc7e7ecb598867aceada', 'crack'],
       'discretemodeling': ['2dc9441cb23df9f087114c4d7873c34fc3bfd9b7b9898219d8a4cda0c1a32fb3', 'discrete'],
       'pskrnl': ['e5610172e5cfe83074b9bb658345237ea30792cbfe487f21222863c650b8c8ec', 'parasolid'],
       'gmcore': ['1b9663795f6500b98b6212559f7e8c176af96499fa90c50011d0101918dc2656', 'base'],
       'gmadv': ['d74120068794abdc086fd33e16c5cfd5a892486c1919ae94aba636e6dbac4bad', 'advmodel'],
    },
    'docs': {
       'FieldSim': ['ac9cf30ef745424d283d62a5d3308bb63a93a382e2d23a6f732d2c3bdd2bdbe9', 'base'],
       'GeomSim': ['41912fb84e01c27c2e71fd315aa46c477c2a6ee8a736e2f446ce83f89a4a051e', 'base'],
       'ParallelMeshSimAdapt': ['03b8c9d99de66c2f52eb16f9ed9379d02af863fd4a3bc4039321d75398ffe2b9', 'paralleladapt'],
       'GeomSimOpenCascade': ['61ab66de85ccdabaf498515710287d08b831a65794e22255cec7897f1b2bb442', 'opencascade'],
       'MeshSimAdapt': ['2ff87c33a8d352ad592d0a5674707dbb15b6f31ae58f3e374d94fcd71fe74a62', 'base'],
       'MeshSimCrack': ['e315f47413d2e7c4c3cefd12201af52fe02f7358796e531c79c2da14032519df', 'crack'],
       'MeshSimAdvanced': ['1ddcee1750850189235f8d040d0692c087b086148fee247c60e2df7d4beed831', 'adv'],
       'GeomSimAdvanced': ['525ed69c4534be5ee4bbb14752a4b90c3fc9eac4e64ecaf81e3520aec970178e', 'advmodel'],
       'GeomSimAcis': ['ccd11c3697cd39a3f751d29c15c7c5196e3d9b823db20f001ce996857d22026f', 'acis'],
       'GeomSimVoxel': ['0df81bb8ed4082124e5bf3b8dcec087b179b9e323966d16c2276db54411efe54', 'voxel'],
       'GeomSimGranite': ['e97487f8c536397838da8950f0dc808976b67099b3f1f0b08168774081632906', 'granite'],
       'MeshSimOctree': ['c2314486a2b36fb516eda73270c4587bcebdeb85616afdfd8776d762a80380cb', 'octree'],
       'ParallelMeshSim': ['9404491fe5ae558db01039497e278a1c14d9f62bba6c0c8a9ff76a073124e44e', 'parallelmesh'],
       'GeomSimDiscreteModeling': ['2559e2ec358514b6e425dcaa18eeaca10f562b7f13391c47fbc2a0af2cb8901c', 'discrete'],
       'GeomSimParasolid': ['0f07b503ed431d8ffed3dd7aefa986052771aa905245669322e82d9eb20014cd', 'parasolid'],
       'MeshSim': ['f10d2842852caee25ecaa512e7f6e6f4e478fee03fefbaa486ee3f4612a386ee', 'base'],
       'GeomSimAbstract': ['0df06212253a4203b87b97e6a9918e1b8ef53aa53b82adb34dd3ce9dcbcc065a', 'abstract'],
       'GeomSimDiscrete': ['f4229431d6e5564810cfe19321e7ec6e6c0bbb2b38cb37826fc52bef4d68bc56', 'discrete'],
    }
},
{
    'version': '2025.0-250108dev',
    'components': {
       'pskrnl': ['3e8f0936b28dd1519d59a5ed2fdcd54c788022052b7704c655645befc96a1bd5', 'parasolid'],
       'gmcore': ['39e5d6d1a296406be87201fdaeb96c60309108a241cb14d66ef4f6141c5eb250', 'base'],
       'discretemodeling': ['4dd0b7aa04e297c90ab7dd75143fa78d980f51c5d1d9563d5d4db6402fd1b392', 'discrete'],
       'mscrack': ['be96d5832f28ceae47a1e559bb2ea0ee89c92817f720d9278fc24af803325744', 'crack'],
       'msparallelmesh': ['3ee3de8e3220b6a87656a7a625e93ff9a0810014f3df0588c9ee6f984d23c8c7', 'parallelmesh'],
       'msadv': ['479ec6e06e220580ccb485a499310866385cf35ae0f2a7a553cf44aca6a3686b', 'adv'],
       'octree': ['df7c80c26cfab91b0697028d29382cc0496890731e48ca97a3e64e9ca0ec5d4b', 'octree'],
       'msadapt': ['f4da00c8dbd77c6ef40879ee9d6ae1425cdbc0cf2eb6d89fd655af29985c46f6', 'base'],
       'gmabstract': ['ecd3a4cd47f9f24dc965ee809c1c3739629e2b9a2ae8eb5ff8f8aceb5af33d9b', 'abstract'],
       'gmvoxel': ['e1e2780ccfd4af0dadd2aba7da8d87a4f009e8f5fd47fc96432d672efb1e9739', 'voxel'],
       'msparalleladapt': ['cbb9982ea61fae8a6d7437598de36ba101aba205489180348787401113227ad7', 'paralleladapt'],
       'fdcore': ['0f4aabc5bafb3cf724701f0da8f7ab258135fc640dcaf86092826506d62f6eda', 'base'],
       'aciskrnl': ['b4f88536e1f41819e170683ac287cae8d12ffd507763d17d110680da74a99402', 'acis'],
       'mscore': ['b4fd3e3421e2faa10aa63ef16bfc74b3def3f02def4b6ef057dedbcdf7e292b4', 'base'],
       'discrete': ['c6333c5a24915ea658b9be2da43b08a534659d0156992e8d8486007f3fa190d1', 'discrete'],
       'gmadv': ['2513b765ec2e98b171a58b23d7d70a382f33bc757cd55a5a3558b37dbd4ca21b', 'advmodel'],
       'opencascade': ['75452d82eff8051dd252d94599f14be13ab5e268da4dfa505a302942bf307442', 'opencascade'],
    },
    'docs': {
       'GeomSimDiscreteModeling': ['6d16101ea4b76eb69e807de461bfb218ad421a8922bd0e2f094edbb4b74f50de', 'discrete'],
       'ParallelMeshSimAdapt': ['b9669a74b4f14125cb8befa6430a870318ae9e1a605516ea7417b14ac9318893', 'paralleladapt'],
       'GeomSimParasolid': ['24601b5800c1cd524fe76a86d47c79546c642ef4d8bced36c09843c48436b2f1', 'parasolid'],
       'ParallelMeshSim': ['2365dad015a270b9e7daa77470300884ed5c665fe605c984fd85658b90cd20d2', 'parallelmesh'],
       'GeomSim': ['836ada057526a1e6ac41515b70d743f8daab7db96d23eaacab9da519226ef707', 'base'],
       'GeomSimDiscrete': ['433f3d287aa4cf900e20a337e81dc08a6ce8666cb8201e9c1fe165641aaa95e7', 'discrete'],
       'GeomSimVoxel': ['e3b2e92ac8a71ec5a92fd160e0d3bfd9f240206b4beaaddbe8bfc389bbbcec19', 'voxel'],
       'GeomSimGranite': ['e99e89d390bac184737053476c26acab5d359aa6c83cf0bbe94d0d1c1abc45ba', 'granite'],
       'GeomSimAbstract': ['fe2d493b7fc978dea38cf2a17c95ee843dd91e1b88e741f58623b98191157595', 'abstract'],
       'GeomSimAcis': ['86681a38dbb1d93d26afad49e9e0b89e47b154855fb8b22a3a827ffd530a36d6', 'acis'],
       'MeshSimOctree': ['f5c8ab3048e576d5f428955e228eaeee267f0f4caca0aadc4f6302d04e64ce2d', 'octree'],
       'GeomSimAdvanced': ['d3cc54cff9c31a2285c7ee06ff05b8a3166f2c6faf3591b647a3d6a470838ca8', 'advmodel'],
       'MeshSimAdvanced': ['6c7c0d087735ce7ed2bcb8901bb418e3a96c8e9be2cc8b85670a16a29c3f0dfd', 'adv'],
       'MeshSim': ['3a8b715a01494879512d16f7491052b1bf7af855d98198ebf0ca7ef11a6ff3e6', 'base'],
       'FieldSim': ['ac1ebd3aa2245e17026394e967ca1daa620214647f40317a652666f8ab5624bf', 'base'],
       'MeshSimCrack': ['60cd763f46d4a2d2feefed03f26e133f4cbacea463c31b01596e241d17fbb670', 'crack'],
       'MeshSimAdapt': ['0928322e3ab5defee8d21b0ea9b70cb3bd5cbf5e923e532c9033353d4e0de1cf', 'base'],
       'GeomSimOpenCascade': ['cf67237f44774e602e7569a50aa567fca2086f6f814d8e533477d034cc831d38', 'opencascade'],
    }
},
{
    'version': '2025.0-241025dev',
    'components': {
       'gmadv': ['16827ef56309c33d1fc6ccf70ada1e810647143f6703931474ff126aba03494d', 'advmodel'],
       'gmvoxel': ['a22e103c92560bedd23029fb34bb21051b2b3165364e65eedb893f112df263b9', 'voxel'],
       'msadapt': ['6c7e7ece11942f5b12d68ec94d25fceb0fa6b11b45fa36084c232869fb02150e', 'base'],
       'octree': ['a655fddf4b9fc3858331c625fcca8fe9b8a3587612ac2252c6ac73bac46314b6', 'octree'],
       'mscore': ['20045244bd5db62572954ee20a5013ce99aa26da715962d2a441d412c96b38d3', 'base'],
       'discrete': ['24560a4546857ef6bcaae82eb5f8c8b4999f4b5f12a653a146354674709c89b3', 'discrete'],
       'aciskrnl': ['6f421bcaaecf375ee785b2cffdb4dd659fd9edbc1ba6f1788dda9193c3d37174', 'acis'],
       'discretemodeling': ['2377ee14814d4702897a969330b8c3b8e63f13b96fff6ea75b8a007cd9fd92c4', 'discrete'],
       'fdcore': ['5bfe68482f080b47fcbf6b35f2b2dafa1db32a5afe8abec17c3e5779fefcf12f', 'base'],
       'msparalleladapt': ['c9d98c48271958fe0c7af9765c216be3d04d4e8e8def5699fa99afb3a46aac68', 'paralleladapt'],
       'msadv': ['a9d30f41f4cb0a064ddfad4f828285e94a7023b2454338b9f628b92ece493ddc', 'adv'],
       'gmabstract': ['6b91d205ce9dfc0b8222683c42c643b04fc745e964a5a16bff64476795ae1891', 'abstract'],
       'msparallelmesh': ['28ed603f160910142f8d1b7700e55d50769ef1f118602702e6f6df9a887213dc', 'parallelmesh'],
       'mscrack': ['fb06867932dc74218f49b1b182fa74b4210d3e6e641f04a4926bd4798b2d4ad6', 'crack'],
       'pskrnl': ['343872962187b6c79308e920320be941b244d54cb06fded0d470850bd1809457', 'parasolid'],
       'gmcore': ['423cdcb644292a7f4514a2c9e0440bcbc3421b23499e36802b7f33a478802f0e', 'base'],
       'opencascade': ['ee0e6f4efec3a10d67a33a411aea98cfa8642b76a78f1a8dfcf2cb55a135e0f4', 'opencascade'],
    },
    'docs': {
       'GeomSim': ['bccda3ed9251ce9f822860215ed1896f66391514ed7afbd309824cd6926b53ab', 'base'],
       'GeomSimAcis': ['a1473c6b52702551ba22326355ea8b78a0489b30e7cc40802822051b5789ba6a', 'acis'],
       'GeomSimAdvanced': ['1335023e1ad4bbb6ad7861bb4f40dc362dbe15a296b2283630b026045dd3bac1', 'advmodel'],
       'GeomSimVoxel': ['7ae83d8feda7d14369bff164105b1eb6c5b373ebf96dbbc2b24e8711f9d277ff', 'voxel'],
       'MeshSimOctree': ['868d943e7a6e6b782f91b5168fb59557fd4521fa60cf7b2e380bbe7f05dd9686', 'octree'],
       'MeshSimAdvanced': ['2e24742ca3e8318aa7ec84c8a27d9d5076f7b8236beabc043b227fb91c49de6b', 'adv'],
       'GeomSimParasolid': ['052901ae303ae8bbdb15f62dcd027332de53a16d3e4d68d2a85a7a51c85996da', 'parasolid'],
       'GeomSimDiscreteModeling': ['3a02df025411831b5d8c1ce4a5f84d3706e14f407caae3d2772f360a5710c432', 'discrete'],
       'ParallelMeshSim': ['c15d73fa237d2c9e2e131ca11399d8d496a122b66ca5ff704b35f49a49f0e7d6', 'parallelmesh'],
       'GeomSimAbstract': ['0818d8cc0a1dd351741a737f0429aa4aaa00d8ab4458f2c1d5873902d4a08dc4', 'abstract'],
       'MeshSim': ['1a45f644c562a5581fff8e0ef7c12f7a146a1418ed816f0f7ca0e3bf1f61e203', 'base'],
       'GeomSimDiscrete': ['1b1176745d92101fa1bdf53d5c78c98f7babdd9893121b23b7668200fff1a728', 'discrete'],
       'GeomSimOpenCascade': ['febbc9c2ae53bb39f7500405827db8b285468689d628c8f4c485b7e5e242d7dd', 'opencascade'],
       'ParallelMeshSimAdapt': ['d333b7654c2a794626f7c14444c39124abdffa934712b415c4abc26dfb36afd3', 'paralleladapt'],
       'FieldSim': ['2dd973de25ba875f774650fe4fb7f722aac0045b870e9b905d7edbd21bf41bc8', 'base'],
       'GeomSimGranite': ['5f4a81cd327bc475cc8bdfa4c13bbba030ef87602c43e3688a21a0015a2482ff', 'granite'],
       'MeshSimCrack': ['ea0b15e6743048b849c3788490385576794945692071f0de45314e8d395e9134', 'crack'],
       'MeshSimAdapt': ['18c10c512abb1b8eeac0e65e6460d8ce72a5d08d9a45c76077f5cf0a2c4b0ade', 'base'],
    }
},
{
    'version': '2025.0-241016dev',
    'components': {
       'msparallelmesh': ['1c4f7183feb74b421d1e71bdde0e2d92bb8231d88f300842ff2bec04ab7bf4b2', 'parallelmesh'],
       'aciskrnl': ['d8306d46a904d6a403a1836ec625e7c7a658588f8c7cb18590b6a8f741f36769', 'acis'],
       'discretemodeling': ['29cd1607a94040b80f314820e1463e4e76c0be6711552f7d1f3ddd08a1d6a2ce', 'discrete'],
       'discrete': ['2cb25392286707967e926356d8307a0a296396ced566cbf9262cec24510ceb8c', 'discrete'],
       'gmcore': ['e26074d19090f259b1a0f14609a77ebe7825d60bb35980de673cb3daf9133f92', 'base'],
       'pskrnl': ['42518417bd22fcb5fa6c32e3f55dd2ecbe2df3e91f43d1a091cb326e36bd26bb', 'parasolid'],
       'opencascade': ['4232b35804be95ac2c69e1057ff57ac75422af83f20c8d5ce2de0d31932ccda5', 'opencascade'],
       'msadapt': ['7b43fbe6d415d13a4ee5e12bf00e4d941220d47c0d098b3adb2981322a27dc6d', 'base'],
       'msadv': ['6659d10b55ed385789fe4df1297e5f775ed82ddcba956370a097d37b4c74a7a6', 'adv'],
       'gmvoxel': ['fcaf19d3d71e2b0af241660fcf3aff160d37158bdde896c2a76f35acbb723d05', 'voxel'],
       'gmabstract': ['34caea8114b094380fa1671c88f533c5ac370c720d06750df6b996af87671a37', 'abstract'],
       'octree': ['02fe95675b841018bba06c833c2b8d709614085d9a714f780fda6d19c6bb8eef', 'octree'],
       'mscore': ['3947781ad2417d114539d812ec8b1b8abfee3e355b82e167c8599abd51c68e50', 'base'],
       'gmadv': ['0fc6916b0ed3e829f794eb256cf361bf35fbbfa62d512133e31bfa89c2cdfc7d', 'advmodel'],
       'msparalleladapt': ['00a2164a96d438e0b76509cd6eaf0ff4bcc20adf5d8eb48dd92d93176258d6bb', 'paralleladapt'],
       'fdcore': ['9cb109afd153903e885a38b639c9bdd47366f14ae8aa7b458b2ab7b7c4293df8', 'base'],
       'mscrack': ['dfdfee02ed52d784cf321f696da8f941b005fee7c1aa4ac77ca4849465bbff71', 'crack'],
    },
    'docs': {
       'GeomSimAdvanced': ['b5b337c9b27a5cdee25d52a5536c8ebca3f11a9db381b083d6b437ece1fc0ea4', 'advmodel'],
       'MeshSimAdvanced': ['cc794bfb5f183f3632f8ab515595c44d9e81a0627866cae28b6ab5a649b52b5e', 'adv'],
       'FieldSim': ['10ace0df717acd0f77d246f2654d908122ed9b1c696ece9a82b8694a523f781c', 'base'],
       'GeomSimDiscreteModeling': ['f2ef45de4ba6c128020fa6ae10e578c0efbd452f6f5e710afb75a64eaad33b7f', 'discrete'],
       'ParallelMeshSimAdapt': ['b796279af831de728e26e03ae25be7e7924dba57c7e03db7a5eb8bd9f444537d', 'paralleladapt'],
       'GeomSimGranite': ['b723447bf8caa1c3e8d1a5974a0f6c006736c9c03ea55c339b763929bf964354', 'granite'],
       'MeshSim': ['5f03de26e4e161bcb6b34336c2b3cbff8ce4c7fa0861591adeb05cde70769a57', 'base'],
       'GeomSimVoxel': ['ac4461398b921afa6888e546e2a17b0df31b812369f84640a1d61c45c2d92eca', 'voxel'],
       'GeomSimAcis': ['f6eb5f526f4ca81a48f994d3c885a8882b320e5a7936aa9fc41d42272f7f0a1c', 'acis'],
       'GeomSimDiscrete': ['3a04b9d69a1574aa35f1ebea0283e351158c2985dca4192ae908079ea4dceba9', 'discrete'],
       'MeshSimOctree': ['1f979cecab1972d298b31f5ff97a41853b66bd3e6555490d5466c3b104f2301c', 'octree'],
       'GeomSimAbstract': ['a255355d9bbf0b6cc83d447fc3891542903402b4b6bdd676a62fca109e3d6c16', 'abstract'],
       'GeomSim': ['c041e5c5f3ca50e5f2a234880849164eb2b8ed8ae82cd135d3b35bcecbc83e87', 'base'],
       'GeomSimOpenCascade': ['8732da989598901f1a6b850a7ae83b23dfac27d4e6d3e29116c172d04cfa77d6', 'opencascade'],
       'MeshSimAdapt': ['3b705d515356db7b716535374728d28c12a83dd9f31b13377b1775d92eff8de2', 'base'],
       'MeshSimCrack': ['dcd34d2708447a2456eea044672d8c8b6400335c98af1019da2c52501607b5e8', 'crack'],
       'ParallelMeshSim': ['2a508976c00ab0da3fdca3a83807139e725166fe0eb3f3b9f29e3e08ada50019', 'parallelmesh'],
       'GeomSimParasolid': ['410ee0d582825ee3b0367a5e668800a46a99912d28460a91f3e2e9f0b3f69644', 'parasolid'],
    }
},
{
    'version': '2024.1-240911dev',
    'components': {
       'msadapt': ['a923589966f572b997647dfa9dab0a2b15b742facd69abf1b04a52eba49b4ad1', 'base'],
       'gmvoxel': ['3e2c38f0cd591c74387cf6e26e862dbe697f31f174bb766db7e72f7d6362834c', 'voxel'],
       'discretemodeling': ['a351b6c1e87ecf5f6cbe43c739415b6b35f49a819c77930badafc7def0374982', 'discrete'],
       'msparalleladapt': ['b0dc70cf353aedb2c261768b3dbac7b5f831edd25e7fc453a29dffe455a423a5', 'paralleladapt'],
       'gmcore': ['2858842759a64dbfb5838d5001cd2c65d3ee9ece8b9c2f309e41007e53c9010d', 'base'],
       'gmadv': ['b24402cf5a3efa1851e66d5ee79bd50188063c7ce6ba13edc19ef3d86bf62f80', 'advmodel'],
       'pskrnl': ['0dd86dd4699292b23fbf865af1466bb7f1aac2b197f793acf97b5b4c52677395', 'parasolid'],
       'opencascade': ['70e9917427ed2263ca1813bc2bf2487b980caea6adc13fdad5cf772313a34660', 'opencascade'],
       'msparallelmesh': ['90eaed800b1241188ab0c2d6c989baba02d2c242ef9dbf894920fb3fda38da11', 'parallelmesh'],
       'mscore': ['280334281a18da5f4a8a253c629dffebebee866d612baa770f05d3f93ecb7740', 'base'],
       'mscrack': ['ba80c5844dfb2603d296a514dcbde419bd0143a1adb5177094b8cc14d1e7d778', 'crack'],
       'gmabstract': ['e5683c1f38aa24d71a4240e234f5f76b9dbb54a47dd1d8035b952d76457b9e60', 'abstract'],
       'fdcore': ['c58bc375477eb708b9b18930ca5b76c91f22968dc7b2a85b996fd4184a47e9d2', 'base'],
       'msadv': ['074055f19d31e1c6e74fb9180388cb6d85588201e40da31e96464b3c59218f11', 'adv'],
       'aciskrnl': ['a57d036fb207182c22e8855143fd94b249517067e476506d13d57195d234ae9b', 'acis'],
       'discrete': ['1eb618d7c06981bfaf3bfd198c1c1a130186228160e8fbd2e8fad25099b1e2a9', 'discrete'],
       'octree': ['09b924b40fb67dedb1798ba2cd4204f15ed209350f78f533912c2ee9a7848086', 'octree'],
    },
    'docs': {
       'MeshSimOctree': ['b5c15a853fa0873ffd910aab7d12da84b778ea4be1cb453d8c2656f0140b4ee4', 'octree'],
       'ParallelMeshSimAdapt': ['fd34a71442ae1015375a7405cd87fe9f0c70739b45661f9cb169ece681fa65fe', 'paralleladapt'],
       'GeomSimGranite': ['a791461be74ef47f2a038e7c3636545c6c1d5e9e4f8acfa306c6994677e6e04e', 'granite'],
       'GeomSimParasolid': ['ad3c2fc2b76cfbc4b94da21c7be082b1c71df5c323c8b0cb87ecf5267088dd68', 'parasolid'],
       'MeshSimAdvanced': ['1899411d118ef8f2f799872ce361283b5993c935d1dc40ba8d554899948977c2', 'adv'],
       'GeomSimVoxel': ['320f10640c6fd95b29658c3e9b392978f3071a560315febdad598ea6ca514898', 'voxel'],
       'GeomSim': ['c002bb47905bc48096f76cfc96a922692082acd34e6f64a3d80208edbc1ffbf6', 'base'],
       'GeomSimAdvanced': ['f4071a2096f992eb60617d5af4ce23b38742936fe9f810a2ae0b1b0a80936b5a', 'advmodel'],
       'ParallelMeshSim': ['0ff5df8a7820bd2b208d626ad47b5ac8b3ed237cac48eae92eb927a4d2135542', 'parallelmesh'],
       'MeshSim': ['0acba80a663b6dd62930ee9d40f1480fc0abf704fc23ec6569d0fef77dae37ee', 'base'],
       'GeomSimDiscreteModeling': ['051b72bcef265582fd75167f5411439e82fe66aaaa8a1b0e30b9fed3ad9bb09f', 'discrete'],
       'GeomSimAcis': ['5b214169b5c1b02e0b365a983ba1c0e9b9b2cc8a0f9c619bad920405e8df4c07', 'acis'],
       'FieldSim': ['f1cee9f3caca5daf88b31aaf62335c09dd3c97d11a524ef7b3f6c53a8c32919f', 'base'],
       'GeomSimDiscrete': ['574a72ac4dd11641471192fa3ef3e43d4bcceb950d5790c49ec481450a718b78', 'discrete'],
       'GeomSimOpenCascade': ['267a8b75e780c6166b28142f852ee9ebc8a2ad89dd5054bd77c9eb8ad862c8cd', 'opencascade'],
       'GeomSimAbstract': ['0b66b3f5329a90ed7db4b6db56aad04f2c2cc9534f63dea9d9b0719651baf261', 'abstract'],
       'MeshSimAdapt': ['b928daf5002b584063f40fd2219a133687b803445d30bb5ce6cf8fdde0412949', 'base'],
       'MeshSimCrack': ['3952e7cfcea3858150dda2eba878ac1e0468cf6522d52fc8f94776768908e81d', 'crack'],
    }
},
{
    'version': '2024.1-240902dev',
    'components': {
       'msadapt': ['f52f64668d028c21e5eb5b22ff8e5e7d32338c894691878d6aff2c0262c1c40e', 'base'],
       'gmvoxel': ['f560f1a338b163078e04e86555a1676e872c68d744c4dc716afca699ee52256f', 'voxel'],
       'discretemodeling': ['17ddd2b965e0c2c16207bd25799522e2fecb037f788e1cebaaab0e1a3f328bdc', 'discrete'],
       'gmadv': ['4807ecd72d6684126c859a31c5992e093216cfa9c712412859764af7781cafbc', 'advmodel'],
       'pskrnl': ['e6429c5f73215461218024713b3e15282f0d5d20022e33b455b7bc51aa918f52', 'parasolid'],
       'gmcore': ['dac5ad7c90582da4ce79a871f3eb865f53fe567aeed20b1891d048252a4224fb', 'base'],
       'opencascade': ['5f452b0dc6aa2a321f502d62916938ce4909a0b3e563390a73ae382b35d63b49', 'opencascade'],
       'mscore': ['3452990fcecc103c4f3a1f56fd9f35e97462f0a1941d5d8182e0dfa994ef8502', 'base'],
       'gmabstract': ['2dd058d84e1288a6bfdfd9e0d8161e8b2ecb9e36e290b6b1358b02b7c36db078', 'abstract'],
       'fdcore': ['5d0f5cba59b431e9ab98570cb14e471a12ccdbff0785e9e3ca5cdb36acdd78af', 'base'],
       'mscrack': ['48565a262bab73232d500bc6634c9eb224202ae0cda75414125cea8e7a0715b3', 'crack'],
       'msparalleladapt': ['890e0cd58aa27b4a0c40913da891299be598d1d7ef4da658633784662ec1ddc7', 'paralleladapt'],
       'msparallelmesh': ['04448abb1a9ca4b85eb94cb39346d61c1fc4088edec7a8eabe5099c9163c4a3a', 'parallelmesh'],
       'octree': ['c79f46410bd869c3f599ea255e718502e7ac06260e5f6d901aec63386685e376', 'octree'],
       'msadv': ['42ea828d67ec16bd815de0683fa3da7073f2deda6bc3cddc24eefa36c8ff0768', 'adv'],
       'aciskrnl': ['1fa20396cd01204795b7469a7507d9bb2fc919719034bf1aa7c2d197b43dd87c', 'acis'],
       'discrete': ['ff2ec90db7cbc6c9b1d9f721928596ed4c3626e280b39f0b2dc9f68017b0d791', 'discrete'],
    },
    'docs': {
       'MeshSimOctree': ['c48069da4726fe53a8cef65d67c9a171c82235b97432b03c972c13cee32625c9', 'octree'],
       'GeomSimParasolid': ['93997b1839f7001682d3a6ceabe471e1a4ad1b63bae93e0ff7878e7f869aa336', 'parasolid'],
       'GeomSimDiscreteModeling': ['fd9b7cbdd3d687394fc06e40e7c7b41608410d3e1b165cf7d55e8f4b9ce49ad3', 'discrete'],
       'MeshSim': ['4d6a12da13cf3d8ec5ef534a69d70eced73151549d58b9a638f9f9e285f4c50b', 'base'],
       'GeomSimGranite': ['82928650c5ef2c609625f15bab3fe9023cee700a63442e8922cb63a2cacbe217', 'granite'],
       'FieldSim': ['39ad58fdfd60971cc68b93fa98ca9154569c93c5edceb7d5551ae949c117d257', 'base'],
       'GeomSimAdvanced': ['8d36212342cb35cc12230b523ff9b9c92e3e052db95ef560a10b66f1e4013b41', 'advmodel'],
       'ParallelMeshSimAdapt': ['8bf0c47c72529bb3d267c08b377c93561c90e131bcdc80abb3f498cf924abf78', 'paralleladapt'],
       'MeshSimAdvanced': ['e1cd2b42659ea8d16307cfc88579d9f47f4bfd551856d185c55e6e53d9c2557b', 'adv'],
       'GeomSimVoxel': ['b17470c443dae59b4893cfd0041b2ad9b536b476264b077bb9f4d4ce449dd8ae', 'voxel'],
       'ParallelMeshSim': ['c6806a6cb9bb8aebb23da7c99d7799a552ffb41394a94057ea2af4d3b3b0b8b0', 'parallelmesh'],
       'GeomSimDiscrete': ['a128f250bc5e3309e81dd21aeb46671aa4babc73ef593d2faf97e48c51194fa2', 'discrete'],
       'MeshSimAdapt': ['8e5c68a24ac14faba96fe439a7793b9466145def9799a3dcf98fe94a44651c26', 'base'],
       'MeshSimCrack': ['c4c914c22a9d7f82401bfdf540f378a1b1852cf8f7a5b98d3894bc86bb4d3844', 'crack'],
       'GeomSimAbstract': ['5f0348b69dbc33a3e4f511ca2c7a1162fe7ea06e0d83022812a88370d80c4bd6', 'abstract'],
       'GeomSim': ['326de62de568ecabcd5bc952f99ba57d258499e944606c8ca4c303352f5a148b', 'base'],
       'GeomSimOpenCascade': ['326669ebcc6e0fb6990fc730c7d81c07f513a54487c4f711b10981a583e4de5b', 'opencascade'],
       'GeomSimAcis': ['5a0860b8a2f2d30d55cb6e141ce1a25889312237ca1c6664aaea09d6499df6f8', 'acis'],
    }
},
{
    'version': '2024.1-240620dev',
    'components': {
       'octree': ['ce34b590e3836c2b107e9278980721362f13c36ca384e23405f248e6db5f9a35', 'octree'],
       'opencascade': ['812fb20d4e03fd158be688ca57db3934d1631716bf42d2864537888ef03d7611', 'opencascade'],
       'gmadv': ['76d5a17e3687aae734e3e48a4a61093336292b1984f56dbaf55033b8e85bed26', 'advmodel'],
       'msadapt': ['524855c8956cfee3ca2e0e8f71c37aace2af4d875841e2a030a2f3bd60bedbaf', 'base'],
       'gmvoxel': ['c1ec8291be682dbd391ef3a93d30032730740ba2b1619bded28d04c6c52104a9', 'voxel'],
       'aciskrnl': ['d9f50c62eb75e68503cd2c5ed251311590f34fda52c362afa590386608c6356a', 'acis'],
       'fdcore': ['9e03b615e9299b6f24345970a3837d347396c57bab2fc217a8d1dfc783d51391', 'base'],
       'msparalleladapt': ['46e3110ff3f341e75297f61699904ba48c478079c21b5d0d5d74357d18478af6', 'paralleladapt'],
       'discrete': ['0f0caba62787b06bb1b9e57373d2eaa41a01f4c1b62ec16fb0ac6e59718209f7', 'discrete'],
       'mscore': ['e3f0b966587730fe369afcb41b115404a3aeeb36f797e436d3b9674f17c5ea00', 'base'],
       'discretemodeling': ['200bb302bcec8b3d54f18f7d851dcb1d5d6464ffe7dd454d838b1dbc9877ca34', 'discrete'],
       'gmcore': ['d300a5ba687a965fadaf0b54485c2f5635337bfefdeb5cfc0b47a3ef0cefdacc', 'base'],
       'pskrnl': ['b07cb8b997c5213302f198614255809004fe1506449b5b9fa82922ae49fff550', 'parasolid'],
       'msparallelmesh': ['6382a31574faa6f35c43e18a9523a4d47506163bfeeb1854b1ba61e409e7a4e2', 'parallelmesh'],
       'msadv': ['218652442cd64f46800f149da4e6d45f1bf2804fd0431bd654622b70693d1d7f', 'adv'],
       'mscrack': ['ff6602cff052665fb823bfea0f31f30e1858f54a2624f6a429eb2018cc917eab', 'crack'],
       'gmabstract': ['84ae7a7a2a3f983ebe36cce57c3079ae501bb0435a417fae74172712225d7538', 'abstract'],
    },
    'docs': {
       'GeomSimVoxel': ['823fb56ba288fd4cfa6f17a63b5e08347279d7a0e47d2cba8bccf990ded8f904', 'voxel'],
       'GeomSimAdvanced': ['5397bf56e67f900201d84ca6270bec4647a47c64f36f97ff2ab55e0feef8af62', 'advmodel'],
       'MeshSimOctree': ['e8601b41a84d2c6b82780d123cd52776fd420f704933d0b0d872176058e1720f', 'octree'],
       'MeshSimAdvanced': ['e088abb0bd63922849e8684580d3819fc6995b7757052f421ce2e057af4db908', 'adv'],
       'GeomSim': ['b225abfd5cdae88deb1fde71a242f93ae2fc8bf1937cb08e517ae78274757464', 'base'],
       'GeomSimDiscreteModeling': ['ee751c03be756be0470bf7e87d005d5369aba0f42bd2ddd22d9f9c285e21ad09', 'discrete'],
       'FieldSim': ['649b00573745ed39e8f0104f98bb9239f784beb99bd1f191eb3d868406652782', 'base'],
       'GeomSimOpenCascade': ['2a1fc087bda630f9f2e3d3f9d0bc8904f994fae9499899d0ca02ef778c347932', 'opencascade'],
       'ParallelMeshSim': ['c419ccbfab792c20f593d3a093c3f59f4084b7b0746f9c27e3653401af077ec6', 'parallelmesh'],
       'MeshSim': ['4bec12e17a82502c5a5fed559bda89733f87d8855f2e75e63ff6e914c6773759', 'base'],
       'GeomSimParasolid': ['bf782f21f2acf37392b25f7ea33c98db3f02bc7515587d0a546b40be8532edca', 'parasolid'],
       'GeomSimDiscrete': ['ab9b2714c356b289468ee7544b6b2f5829695d6088fa64ad5bdcb51770177915', 'discrete'],
       'GeomSimAbstract': ['58e5ca24ca02db83209d96ba85ed8cb06787f270d6c7e49b287e3248b3393476', 'abstract'],
       'ParallelMeshSimAdapt': ['2dcc42a33b1cb3e704061f51f1acea9b329f9f8ce0c24536a6b9f401706e3656', 'paralleladapt'],
       'GeomSimGranite': ['b7b6b7296479dfdf025c11beb86130c757fb0e666303c542628bbdacfae89db0', 'granite'],
       'MeshSimCrack': ['2271e10fb3df83033123d85e7add729541cd95d1e1917f8106de6d7cdebe94cb', 'crack'],
       'GeomSimAcis': ['0d7d775cdf3347ae8b6712e97d49198e367be0426ee142f443bb269695c3a987', 'acis'],
       'MeshSimAdapt': ['14e7c64e0f076e8c390cc3a955d0cf1d2f2de8578b1fbe5c0d5c7332cbd97116', 'base'],
    }
},
{
    'version': '2024.1-240606dev',
    'components': {
       'discretemodeling': ['706e11975136e9ed21ffca7ba271079fe4a62339f01de6b2cd31ffafd5baaa3c', 'discrete'],
       'gmvoxel': ['24b954e55a7a066cd34806250cdc56e6bbbcdb1de0b9e17ebdf2f61a93146677', 'voxel'],
       'msadapt': ['f837440119fcf6dbc0efca8cbe7a250faaee67e00726cc912f8b65a0f88a0c1d', 'base'],
       'gmadv': ['e96e8e7e5cb334039d205dc6a458882ca9bd9d69c089c815f0664b1f3e07d2b9', 'advmodel'],
       'gmcore': ['db58615837eb4088bbd050054beb1afd2c3ab57388ec7bdf87829a75b7677e44', 'base'],
       'pskrnl': ['50c4f542618216d55bcd621cec7a8f3772948174a2ccd452c507a5b07411e1bc', 'parasolid'],
       'msparallelmesh': ['ab979111a0ce41f0bcbbb5f4d66cbd49ee76caa1cf2063d819dc0e52955ac0a3', 'parallelmesh'],
       'mscrack': ['4110277d50083da50fdc05947b1687af17109630f9b266b1f253ea59fc768a30', 'crack'],
       'discrete': ['d1844c463e3a7ca73e1a8552dbf9651e9e1c189e70e5258bfcd65af70c936eda', 'discrete'],
       'mscore': ['6855d55bfd56caa280bc79291b622968ef6018df1a186777e6d73f264c2feb45', 'base'],
       'msadv': ['f551258439fc3aadc4934cadc1b9dc556724a5107d48a4ae3057154840ea2919', 'adv'],
       'aciskrnl': ['af2f2e2a4779043cd8c7dafa290b6257d5c5abb0737823a82613e01efce418fd', 'acis'],
       'opencascade': ['cafc3f77d559ebb4376b84d27877af8b978f9941a1c34c5a052fbef7433f6ecb', 'opencascade'],
       'fdcore': ['42e2076c729554a0b70cdfefaddf88c9897645a4ffab32b80401b73a401a361d', 'base'],
       'msparalleladapt': ['7d99aaad7db45835d583502e920dad5ea626615d85b17860018bd0f07e8a5998', 'paralleladapt'],
       'gmabstract': ['b4b1ce19c9208decbc501150fb35ce3a08e7b44a923a32d7e6aa77feca10b604', 'abstract'],
    },
    'docs': {
       'GeomSimDiscreteModeling': ['45f73550a156fa780cba401eab1f1e2aa5a412724cd664e917a379800262e71c', 'discrete'],
       'GeomSimGranite': ['a5ed955857720ac8c4b01a5c0c426e1e83b09d52601c8218e87796c737d189f7', 'granite'],
       'MeshSimCrack': ['34ae1fc06da4e1c88c855afecbe0cfdf6275fb5f1c3e4f20c80b5bf2aa6f642d', 'crack'],
       'MeshSimAdapt': ['7d05317f6624b9fa875c61254f2256211f31e8759491e5e9a743ffd743653646', 'base'],
       'GeomSim': ['a6793581bf635eb6cf3ec420865643dd8ab1db045ff6a1b91833b5d6d3f6ecc2', 'base'],
       'MeshSimAdvanced': ['266072e3e6699d7fe94abf8127713ce8ec617444a3fdbd24f69759eec0c60b80', 'adv'],
       'GeomSimParasolid': ['e2758d85daa09cc18d81e8ff9186ea690470cba646135b2648eb5f0fb66103aa', 'parasolid'],
       'GeomSimAdvanced': ['67a5824b00870d5f8f2d25ede1a84b9f3fb607411ae2fa33e5819ead07afaee5', 'advmodel'],
       'FieldSim': ['81185aa56fecee60a957788e43307d55109fb29068cef1d09607821e2eb1801d', 'base'],
       'MeshSim': ['486798ea0222aae409b5ce76ce47bf5c60a16c5ac2b6357230524bbca875ac59', 'base'],
       'ParallelMeshSim': ['20f600cf79b15c723620438aad0c3be68026e77062a04c13538cb36e92ad4049', 'parallelmesh'],
       'GeomSimAcis': ['d5e14147455ae131ff52e7760a9868d194db51cb4579506c72ab374b3b1f54b6', 'acis'],
       'GeomSimOpenCascade': ['eee3d9bd73d43555c33497cb2148cf1f8d316cfb2d207ce5c7cd0b838c84fdb4', 'opencascade'],
       'ParallelMeshSimAdapt': ['bb6a9496004a2ce666a60637c09d4b292ff9ccedfa431f41406c31e9a6680e50', 'paralleladapt'],
       'GeomSimVoxel': ['65b138c50d6fe47fa99fb3f42f31de9cb57b891a57376aac155d491485c5ee9d', 'voxel'],
       'GeomSimAbstract': ['e6d171606c8dd1612823b400082d66bb98d77a2ea4747e0ad503dcfcc9c172da', 'abstract'],
       'GeomSimDiscrete': ['6fc39a0cb920b346f69ec2ea29ed9110c88fcc476d6911777f7427a10fa3d643', 'discrete'],
    }
},
     {
         'version': '2024.1-240522dev',
         'components': {
            'pskrnl': ['3d1f4fc4fd8afb47a17f901c445a6ef1bfa12da0b51643b793243fe9cdd3dfd0', 'parasolid'],
            'gmcore': ['e396e1bf30435aac0fbd5bb9671ecee40b9be88a62cbcc1dde1c19101daceeeb', 'base'],
            'gmadv': ['f32fdd66e76a6a6726fca314005448f56ceece910390b7bc59672b8ea4c47e07', 'advmodel'],
            'mscrack': ['40a9717afab305f9fa9ddb630d7f4ce208b2be793852eb1d5dc7cb4c8a53c572', 'crack'],
            'discrete': ['e2e1bdee2359ca36eb10f1c1a5528bc3b6f7ba8d5b072fe69630bec96c35fc42', 'discrete'],
            'aciskrnl': ['d5d2e4ab90c6c9e484c0641ffe128cd621120f41fd6138d3725e1137111a0407', 'acis'],
            'msparalleladapt': ['603f2888f17077266f42c663d36737164b9ad80b7628a8b729c734eebddb6816', 'paralleladapt'],
            'msparallelmesh': ['10b11c68486ab6ff090fbd7272152effa9917ea90ee2f97c6b74396e3a60714e', 'parallelmesh'],
            'psint': ['ab9c1f55bed777f55eea8795939daf382631dc00c423e798438480a7c21bab2c', 'parasolid'],
            'msadv': ['4c81b4ecb01eec689cc5d7e906aeb21db3787b37460c08989eae6e528f2c7206', 'adv'],
            'msadapt': ['bf2deb736dc93650ed2a05081591aad002aea4e0a32054cec80045d7a98ee3e6', 'base'],
            'gmabstract': ['18c3bc327ebec732fff351291ffb836717b7fbdbe6c17b4befa5671e21295194', 'abstract'],
            'gmvoxel': ['7eaee76a38bd603c570720664415567fa06e9a7e0f2376a4b9d488f7af4d3cf5', 'voxel'],
            'fdcore': ['735fd20a951024aa623e70060c276c09682db0527468929ec2ba2581c4fefc4a', 'base'],
            'mscore': ['7918c26b9da7bc51288404c463b4438d91ae37a291ec4714bd5172fb6e13f3f0', 'base'],
         },
         'docs': {
            'FieldSim': ['ab8f08cefcdc6fa71681aa012ef6b1908769652934fa10a888ae2f2bac805eb0', 'base'],
            'ParallelMeshSim': ['0e69346b716d9862a67ae0a938d7869c76591fa71ae2a090e2aa27d265b8ffe2', 'parallelmesh'],
            'GeomSimDiscrete': ['769851ae1ad1d4da96df97c7cd4a64865e964e06e3ec870cb399f7956e749484', 'discrete'],
            'GeomSimVoxel': ['c59fb2e278369850276fcfeea739d374f14da6b2d3d69c57f4aafa0a3da46cfe', 'voxel'],
            'GeomSimAcis': ['733382ebf4d4632f23ee75d69251e969b68bbc9c7304ef3ac47ea19d92d102f7', 'acis'],
            'GeomSimAbstract': ['1884f67a1d6a35843f95a0543b6a5cc8f848de8d1a78fd9ae23ffcb9f79fe6a5', 'abstract'],
            'ParallelMeshSimAdapt': ['d6ee66be36fc24c4abb1808b7e3ef9c132abc24b24f4aca6d8581e679927b941', 'paralleladapt'],
            'MeshSim': ['ba6644e41c4d178bb2440af74ef9812576e7bc2d88502ed12bae06192e5c0d3a', 'base'],
            'GeomSimDiscreteModeling': ['d5d73093bef00298895dd2df3c19e1411a56d169dab2bd7a9b8698c97c531620', 'discrete'],
            'GeomSimParasolid': ['3539cd3f886f072b61fb4a11d7743b9cf6e06dc22498386e5e3cb5a8046de006', 'parasolid'],
            'GeomSim': ['f2d8553318b8a8477fe20ef0bebec04844557b2a56af24f27364d90f7e3e47b3', 'base'],
            'GeomSimAdvanced': ['08cbe8ea2fb28e3895e10f60f57c472cf33c243e6667174477939855906e78c9', 'advmodel'],
            'MeshSimAdvanced': ['623cce7c69f5f65ed6f2509aead371e137574456c0bad956d1ef78bb94706e71', 'adv'],
            'MeshSimAdapt': ['fc5b8a0008e0e5160e072e0ca35c75b016a19bd295709306fe9966b5ff9630a7', 'base'],
            'MeshSimCrack': ['ffcb50ba88dded7541fe39c633fcb34ae7a99d885bb30bff33b841a03256a228', 'crack'],
         }
     },
     {
         'version': '2024.1-240405dev',
         'components': {
            'gmvoxel': ['c12126e6d945ef123998f064274ad14d3896cec28625fad40ecb9eb9d3d2be0d', 'voxel'],
            'gmcore': ['0672e59a3c6afc63253227994fc9360f1acdd13674ebbde1a363048696cb15c6', 'base'],
            'pskrnl': ['db094fc44869e1920b56d9c5a40621e8269f7c5f26928780b761c74a3c9faca2', 'parasolid'],
            'msadapt': ['50bd9818a44a08cf1c8d54de85862f9e3022a1b55d24b7c193fa0bf1e467084d', 'base'],
            'gmabstract': ['e1a1136db4e9df644b5d45cd85373ad1bfcf24e3838e3183d2df67d263113aee', 'abstract'],
            'aciskrnl': ['b7267967eb045338b4e5734235b35610ce21f1c1ce61c87f85bc14619cba7963', 'acis'],
            'psint': ['a02676ed1d37e097bcb36138ec1030e9541de689d6b286ba1c4c69d7975225f4', 'parasolid'],
            'discrete': ['d66e7bb3f235b0a952e814abfcc91ed86928101eb083efa8c24ab7ddc1f495eb', 'discrete'],
            'msadv': ['b312e3328e652f706ba81edd8e50957c68d213b608fdc9eb9e72e3ec0d3f619a', 'adv'],
            'mscrack': ['56ada1006e3aacda3b6d97a3f035738ea2f39389764ec2e4559d27a947f3d928', 'crack'],
            'msparalleladapt': ['2c26c588fa576e1d1b5d7ac907764a517b66a68153c0f8248333a90a2fdd8bdb', 'paralleladapt'],
            'mscore': ['b75a6c04849368ff7abed58933234f78da5cdcfb9200f5824bf080a3e3f5558e', 'base'],
            'msparallelmesh': ['51bece6c3b73218eccd52d7d757a61be5c1232116ba91f96eb5a47b164494cf1', 'parallelmesh'],
            'fdcore': ['55df907231026574509e17c4a11b66221b1c22fbc737d63ee4305e05967f370e', 'base'],
            'gmadv': ['bfc2ecc4667f97d483ff0d154e39f172c65a15c1293e78242e4471792de006b6', 'advmodel'],
         },
         'docs': {
            'GeomSimDiscreteModeling': ['b6f880276612ab2fc0b6a5c685251ac19e63ed9c4b7339a7e44233301269cbb1', 'discrete'],
            'ParallelMeshSimAdapt': ['963f2eb84ec83d4389a39e8293dd3f84a00dc72b7a2acb25ef4b1cca5244d163', 'paralleladapt'],
            'GeomSimAdvanced': ['fc2c2b23761a3e24d15e35c1e1184037c0da8d1f855e4a9ab9730c9a36ffb5d7', 'advmodel'],
            'GeomSim': ['4c1c25f4fa25451da761f4d879b184ed9a9c7dcc363bf92b997950140cd3e7a4', 'base'],
            'GeomSimAcis': ['0c1fe16a372d7a6a4d4d4881825ec30fa1ad966790b0141f657965a6e47c06e6', 'acis'],
            'MeshSimAdapt': ['91eec4eaff5094e990e14353c09f815a0064991b1388c8ac02e6f875058feb89', 'base'],
            'MeshSimCrack': ['fa827006703cecd8930eb3b7f84b5670fd2fb3515f8baa93e91ef15d32136778', 'crack'],
            'MeshSimAdvanced': ['ad7fd2a69d744d185e291a10322aef93f737e1628c11dfad1f04f3a31cfde1e8', 'adv'],
            'FieldSim': ['60881ee195e6695c87752d55cb6b2ddfdb294b521c4bcfaf9fa11364fe8c8cc9', 'base'],
            'MeshSim': ['c3def9b003425927c5369545f2173dbe3165f1218ae8913a1dc404b04ff9e77f', 'base'],
            'ParallelMeshSim': ['8ffe5252dbb1cb98313df35f0f5a1075637c5a11acd4488b4ebce9540c13ed79', 'parallelmesh'],
            'GeomSimParasolid': ['fa28f2921483e9df0a8ed2117585e8974db9633f572b31a2b0e0209a96457e3d', 'parasolid'],
            'GeomSimAbstract': ['af65f656a016f59c562c60fa4b74978303e5d662ef0a64dbd879bf05e3949c51', 'abstract'],
            'GeomSimVoxel': ['4190d7dbf0cc3e24776c60f6e22ee1a2bbbfdcb7cdc6a12ea614146b722cabc4', 'voxel'],
            'GeomSimDiscrete': ['2e129c1903fe5be0fc778c40f5e171b0e341072fd72f120263e90c6a06639ae1', 'discrete'],
         }
     },
     {
         'version': '2024.0-240402',
         'components': {
            'gmvoxel': ['71238e866ab6d4d42c7d3c53643902284d4c1d9cbbf1d07e1e188ca263a104a2', 'voxel'],
            'gmabstract': ['31aaf61623d0374001bf12cb10a5d94c1b0dbaf3f617accfdb399b616bebe589', 'abstract'],
            'fdcore': ['66a78de6d4626c322e899b450c2e4f8933785589cc06f582db6484278b892757', 'base'],
            'msadapt': ['5ab81e32027dfe0951f6f561c4b5d02b0b0e117d70ac502103e1fa73eea099a4', 'base'],
            'mscore': ['f33ed3347ab233662341448197325b9f05900dcf498f776003047429ab338899', 'base'],
            'gmadv': ['3dc6db6fc49818aa877150bb634f4d55c8bed1095051602c1f5620f8f9ec7b1d', 'advmodel'],
            'mscrack': ['0769f79a94812a92a4ea80faaa6f3e8e5e31ce4e4aee61acdfe7d20030a9ad61', 'crack'],
            'psint': ['53b23d6797798a1b661df57dde39d14a23eaff33e371847889d49263de0f1c33', 'parasolid'],
            'msadv': ['305cc34e9c7b6261fa03e10e6636e488e4dc95e2605178beb0d6a922535dbf17', 'adv'],
            'msparalleladapt': ['413dcf4d7601ab4f6c01f1f355d06a00815f2270b7829d26f7a1e27811303324', 'paralleladapt'],
            'discrete': ['bb806bd2b0ba9157f011fdcb93ac21a108411220cf6d70cbd6756029ad713691', 'discrete'],
            'aciskrnl': ['d7c9a6973fa7b44713658ab0aba854a7353ed009dfc7c3631be9cec221701666', 'acis'],
            'gmcore': ['024c80884b59e3f1c780bb4c3910c7a30c91167a5fa45e54b84efdf7cf60aeb0', 'base'],
            'pskrnl': ['10a6885f48825d8cfe2846ba71b12ce224b19daaa23134f17511bcd89fbe5d80', 'parasolid'],
            'msparallelmesh': ['f42889d6347c09785dfc9ec526e7bee09b9221b8468c0d0d101f2c1d1215cfd2', 'parallelmesh'],
         },
         'docs': {
            'MeshSim': ['ed0995d1d060faf346b4e06c7eef3a42a98c5a2055d4c81d11ce7fed21c32a79', 'base'],
            'MeshSimCrack': ['1cd01ceec83cb092fda4d4c33a9c8523e380addc5b0749e10075bdda163325b3', 'crack'],
            'MeshSimAdapt': ['3002d44ca8fc66eb260b172f5fd3cc18bc6c0f18f6438e4f0f17696985ab2e2e', 'base'],
            'GeomSimParasolid': ['00bcebbfda3c5534e58230de5cd8e96abb67d4da89986186787183b1d32c1af1', 'parasolid'],
            'MeshSimAdvanced': ['29630b5c993eb675a728d67c6d32dc56cbeccc403fc7c1d8be77d6934128e97e', 'adv'],
            'GeomSimDiscreteModeling': ['3cee419802ce16808aedb163243821a28c161054d30d44b50f22751be1a7453d', 'discrete'],
            'GeomSimAdvanced': ['44b74897ad789a47c4efa4ac4fcb737a117761589b2314a6aea1038086844e15', 'advmodel'],
            'GeomSimAcis': ['094ca16d5807b520616af425e343d433abc46a36b9170677e6fcdc609b499766', 'acis'],
            'ParallelMeshSimAdapt': ['222193bfb32cb5efe89eae156c8db288a33c3291bca782c1f92f72ddf848428e', 'paralleladapt'],
            'ParallelMeshSim': ['fc6bd75376cd95c3fa03804379867189bea36e42bb85eb84db9fd4be1b5eb34d', 'parallelmesh'],
            'GeomSimVoxel': ['c49d1b567cda17641ef2857dcd16a33020b3bea7f3957e1d50c306dd20fa748c', 'voxel'],
            'FieldSim': ['998572b7fab810dbe1ff133f21cca468beb8bafed219c307d5853f2cf9be1293', 'base'],
            'GeomSim': ['beea854ec8ddea58687863df4f75bbb3900f710881993dba478961e064a4a7bb', 'base'],
            'GeomSimAbstract': ['99f241033924e715a1beba5b64d6f6f29d25e8a0de42ab5792e832f47cff8315', 'abstract'],
            'GeomSimDiscrete': ['75fd0acb3107aa8501b4520ffc548b0ec56c585dbd0fbbfd5001f9d9cc904f72', 'discrete'],
         }
     },
     {
         'version': '2024.0-240219dev',
         'components': {
            'gmadv': ['9c853d6a6e3f597cfc326a3ec7a291660ebe0ef7b54b393ce5b3a0867595ae6d', 'advmodel'],
            'gmcore': ['be174632e11a663c2f2ca85302e90c0de446fe5d37cbabe472a342930fb38d05', 'base'],
            'pskrnl': ['42b1ddd01af29af5866dfdb181b83dc68004f191ac72ed75b10c437045f3646e', 'parasolid'],
            'msadapt': ['58c94bc949362d8f47ab955d67a4f972d38b9f28c17dd2531bdbac82c61b5d30', 'base'],
            'gmabstract': ['9f3c18a1432e032cc51a1335da171b22323ff4f3b6306c5d18a09803d8ecdb4c', 'abstract'],
            'gmvoxel': ['6711eb5062f8a2933c966e11f4eaa7ad2aca5cc974ea7be68754d9a043d70748', 'voxel'],
            'msparalleladapt': ['7860c8f0ff80b7906def0fd68ef4ae55d62e045fa9062068e1eef67c1c39a2da', 'paralleladapt'],
            'msadv': ['46a8c45f2af8961b82e77e6ab55c296fa7b43bf1b55750d83dad45213ac6b567', 'adv'],
            'psint': ['9cde3a6d9f829e124dc2b0af5a63b028ea44a098f618d525dd2ea5684d481d6a', 'parasolid'],
            'mscore': ['fd972f20c71af7f31f38a15abd44003acbfb664d34d5909610becbd65d5ce57b', 'base'],
            'aciskrnl': ['31f4a63f39c879351ff017ebb9e4758f7e41d406e7b37f89eed6c19984432f4e', 'acis'],
            'discrete': ['3f0d9071a9685492b7750cfa29516b08e7085e25f98593265b0f89c7d7bf742e', 'discrete'],
            'mscrack': ['c2facb2c1e353d87ff7510319aaa623d671c3b3d4275904f202cb13b95b4f20d', 'crack'],
            'msparallelmesh': ['11ef502ce2c8f1a3c894272277e9da48dbfeca8ef71face622e84e5add68fe5b', 'parallelmesh'],
            'fdcore': ['4283ef966ebe9bd90b94b507e6106a4b19439a0bd4b20ab8ef2a3aa6129cedbd', 'base'],
         },
         'docs': {
            'MeshSimAdvanced': ['ec14b0d8a98eb79c3197e31ebbd4fd07fbb7a52c375a94b6c2328072f4eb4f78', 'adv'],
            'GeomSimAdvanced': ['bca7df73e0c360ba4ca4f7bffbd15c0d6fd01e46ea8d798ac504755ca80627f9', 'advmodel'],
            'GeomSimParasolid': ['04184438094572a3598b2b1a733db6c663280dcc3a456a2a35c4a40474e168b1', 'parasolid'],
            'GeomSimAcis': ['6c5e49c19d3e84a80bee86876c7a3afee50aab3463d42144b06ae07bffd98a86', 'acis'],
            'GeomSimDiscreteModeling': ['00ed957c2f3b51065aa0e3a9d10aa65c3bd1d9ad7530564833013963014e608f', 'discrete'],
            'MeshSimAdapt': ['3b58b12488971c652d4d54fca7b1e24cfd3b0aca41ea12c0d6ede0f86bb5db12', 'base'],
            'MeshSimCrack': ['f198a0a90ab9383e9ba9ec48814646f07b64801f5b90bcc343c1b99e2ba2ea71', 'crack'],
            'MeshSim': ['544b88863583a3e7baa7c4bafab45a038531fbf7a309ec5bcb5e1494345998e9', 'base'],
            'ParallelMeshSimAdapt': ['56663809cd56528b87247ede2ccb456572599b2d1ab0a8e831f921847ee74030', 'paralleladapt'],
            'GeomSim': ['7ee2e228328de21298c64d92312b4d277050f17e9301b3bcd51ebe8091fb28ab', 'base'],
            'FieldSim': ['7f68c72506e0faebfa1aedf982f68e21046035d460d29c222787a0d01fe6e8e1', 'base'],
            'GeomSimDiscrete': ['216dce3fcafd76a2cdb7436a9e9b6de0641960ed6d74383bfc837d397a6f0429', 'discrete'],
            'GeomSimAbstract': ['f955383f2520349bb8a976feb96599aca6d2bc15bc1d2ab5da5e886f49d926dc', 'abstract'],
            'ParallelMeshSim': ['39f4bd2443178ea9dca883e72d006c18adb8b338b6a50293b6a6118562f7169d', 'parallelmesh'],
            'GeomSimVoxel': ['a747b16ea9d12698f2ced1e145c00f4e716d871e63725a65bf0b3a3159251b99', 'voxel'],
         }
     },
    {
        'version': '2024.0-240119dev',
        'components': {
           'gmvoxel': ['84fd3411eb6f49ce102009e6d89f6b08b4b0c06941844e3fe7eb84ad8de135c5', 'voxel'],
           'msadapt': ['8888b96ff7bdcabc75ace4120b210e6644f37882d2c568560ac1b4460619b538', 'base'],
           'msparalleladapt': ['477af21f74d95587d4ac9782e8fb380a90fd384e5b0cb9a9915964807d3b83e2', 'paralleladapt'],
           'gmabstract': ['886d25c8cced465ca656266fed6c80280e0154fdf6517480758d89cd93cef35c', 'abstract'],
           'msparallelmesh': ['9b90244e37f20a717c31fab999140dc3232e89e7667d4b900268fb1c7d956e33', 'parallelmesh'],
           'fdcore': ['0684bd98b7b362ed5c8740448cef9d59f17e4a520038f06f5964a4d600cf25e7', 'base'],
           'msadv': ['08a40a9ecf70bd86c2cd427f39aa2ee18ffc70591ce8f96e26a8ae10e149c6c2', 'adv'],
           'psint': ['72664de2f9fc76f07676ac696e1420c36b1eef79c097dd203be2c0918508aa40', 'parasolid'],
           'mscore': ['bb673e57000f66f8c9bad8f58529ae002b7f279f61335e146c79f0b037fd822d', 'base'],
           'aciskrnl': ['f7119a10fd54be7e3fab37b51fcbbbbd9f93fad00c234822971c6c09d07fb89f', 'acis'],
           'mscrack': ['63a3aaa9a5c8ddb272b210bb8f0e41b9ef71d6336203eb61d6aaff5360c98aa5', 'crack'],
           'pskrnl': ['f9a1de83cb6ec60093cf57e729144c7cf4005b89e83c1ef559196050e690e0a7', 'parasolid'],
           'discrete': ['d57f5a62212c04efc0c5b32a5d11972685ac3baf14149f5f1e3e952238b0beab', 'discrete'],
           'gmcore': ['9e2551df5b4b905bdf568ea1577e073934433dfb39aaf26149b3ffb7b94f27d2', 'base'],
           'gmadv': ['2bb5194a1894e54278c1cc12a7c203538a5f3cfcc855092204913f6fdc1bfb0b', 'advmodel'],
        },
        'docs': {
           'MeshSimAdapt': ['39c2d171871d59d35258e7075ba2e641178e6460f99ce9d39d9d3112d1d06ccf', 'base'],
           'MeshSimCrack': ['b28e5db7af7f4dbc025c0055e399c5587eaf3d1c5309823628a12040b8b8c76b', 'crack'],
           'GeomSim': ['5ce20c44551948ac1ab13097118240f50f959e87693303634f8ba388f9b42544', 'base'],
           'MeshSimAdvanced': ['78a73520c133ff8d63473c95a4a5fa01429305ec4f2fa6ba9560e57294c34d4f', 'adv'],
           'GeomSimAcis': ['5f8ec82506953d95e20d5405dd18fe18cd7234dbc393e4ff30ccc44ca2a2c42f', 'acis'],
           'FieldSim': ['86b6021154885861ed4dece027be1bd33854c2edf7e2ad02f915c7fd566f26ca', 'base'],
           'GeomSimAdvanced': ['c5303d24e5a9d504968b6c53ad508740398ef53f10aad966631a1bbffec48820', 'advmodel'],
           'GeomSimParasolid': ['ed1cc111adfb73871d52d7f6846b10ac5f451a867d5ddfa86d6d33dc42cd2e46', 'parasolid'],
           'MeshSim': ['fe7df052ee48b65fa70b70584a2f6401af2fd80e38ed4c66a41dff67a62d8a0c', 'base'],
           'ParallelMeshSim': ['78a59881c94693436fd049183e684d8c4dd9cf8d1dbedca23ca83c9d82d85b96', 'parallelmesh'],
           'GeomSimVoxel': ['73afce0d7fb2f160d46840087cae2e96544f5b37b82ecbc29dd66949ec6050c6', 'voxel'],
           'ParallelMeshSimAdapt': ['f51ca94e1e65b16aa43627dbc4fb069e21d70d852b54c9752e5083d75656d620', 'paralleladapt'],
           'GeomSimAbstract': ['0f68030ae6c69d6923a75a367389a621e053bb405b1da04d2795796313b55f33', 'abstract'],
           'GeomSimDiscrete': ['436b5817fd22317d5c1f47e8b27bb855443157f7313cc9b329d1cc56ef73a7f9', 'discrete'],
           'GeomSimDiscreteModeling': ['586f1259fc012491c60ea993c785119351d90383f6df4a40bc903dc05732e8a1', 'discrete'],
        }
    },
    {
        'version': '2023.1-230907dev',
        'components': {
           'fdcore': ['cdb3e937c064ebfb7f8c45b5de7cff7e4ca4a727d3a33e979f62687dab2b8bf8', 'base'],
           'mscore': ['38b3e9ea02872ac0a760df5c0cb9999f6afef43905a9a78c9a63ce79e3b2c176', 'base'],
           'gmadv': ['ab942e2e9f118811dddb8bc812b662b752176a6aa61f16847d713e8e197469f8', 'advmodel'],
           'msparallelmesh': ['2bb9d824d1cec9a9b983713d0f4cb980e44a99d8f25f74ae87d3162c8cabd9bd', 'parallelmesh'],
           'aciskrnl': ['c8512becbc1b42ef2a787f0144b5bace01753c9538f4a39efa6613c3998fae56', 'acis'],
           'mscrack': ['d51f979420026f987795c538c5365ca6243a69b1dfe481037f874e7abfc53ffe', 'crack'],
           'discrete': ['0fc27c2705ff5d90f3daa8bca25288f83326a33cc39f4101465bb7df346b3617', 'discrete'],
           'msadv': ['4eb40f73181219336b57e8c6b07eb64f43f8e99b74ff19b447c0d72e9e821e8e', 'adv'],
           'psint': ['d660e3a79f0912de98fb94a585ca106a2027d1f14b2eb586292d5b5eef24261d', 'parasolid'],
           'gmabstract': ['0204acf10f39feaadcd34e99a4603d5e92a37b0ec2357c0d0134ec8397fe184a', 'abstract'],
           'gmcore': ['3fd94c35d6336ccd22f6925c994907608880eb0ad11db188a87f12dd40f373c8', 'base'],
           'pskrnl': ['c36423e668788a77669578cf3a0919ace279c7fa2fcf640964dc8e5b002bf109', 'parasolid'],
           'gmvoxel': ['26535d3482ff975a5270ecff093c4bc3d9ebf3eaf1bce2d0bfb0f6c66a2431c8', 'voxel'],
           'msparalleladapt': ['80457230df9907f001deedc3aa50dc28c4d19e775fe466fa7c54648a47c4e65a', 'paralleladapt'],
           'msadapt': ['50fcf225404f7f42c703db2d44687075dd4ce410449ed0c39864224c2b3ecb1d', 'base'],
        },
        'docs': {
           'GeomSimVoxel': ['84aff0bd3d30e29992891ddf3fddb566dbc485ad707eb35e6474b8ad9ebe1143', 'voxel'],
           'GeomSimAbstract': ['9f9cef2df87eb551a2062cc501e78b8a53d110e739b5457622cd0f1797f439fa', 'abstract'],
           'GeomSimDiscrete': ['8e8a6b4a1be69fd70c9be08d7789628a1986928b3f533d477f22dc1aa88d5579', 'discrete'],
           'GeomSimDiscreteModeling': ['483ad15c37647688e8c9b7e84b6c98f66f43bad37adcab54d60b78a348679a32', 'discrete'],
           'GeomSimAcis': ['c375a01c086e3a01b27585dff6dd94acf2dff27e54e168c69515e2b7364ae2cf', 'acis'],
           'GeomSim': ['4a09ca7a2eb54092cea58f56e8ae5a56e2bc5d2f53b8aebca9ac24d4d0c996c7', 'base'],
           'ParallelMeshSim': ['f0b4136346668bba3998f5dc21468160897e7abe9bbb0fec43a05444968933ad', 'parallelmesh'],
           'FieldSim': ['28a3788c63b4750b50309ba7876997e5623bb00fb3e22fdf8f66126a29f6c618', 'base'],
           'GeomSimParasolid': ['f769e7d91a5d8023c61255c97ffb16823f5161a537bb93d236681d7a80a2c9fd', 'parasolid'],
           'GeomSimAdvanced': ['67e7b68d794d8ff564353fdddd54dc08fbdb01cef99ee9779763cdcdb4d6e656', 'advmodel'],
           'ParallelMeshSimAdapt': ['2948739c44b363f7360f77133f637b1198314f9da591ebd4cc11d81dc1889a00', 'paralleladapt'],
           'MeshSimAdapt': ['245b6fd49c2cc3f51c474f2429cb0f8ab0387d610d1f3c0434f4069d181bd024', 'base'],
           'MeshSimCrack': ['545c3e151a3b246ce180833c07149062ca4002f16ecd94ffbd64fd1a325b020b', 'crack'],
           'MeshSimAdvanced': ['dd8f9d684e0bd1acf6c7fed7d40b25084b65689b27881e2c4104c69aea566cea', 'adv'],
           'MeshSim': ['0e638eafc6eb3d695d6b29dba1f15fa09b6d48b4fe5f9ea806c884d6824b11eb', 'base'],
        }
    },
    {
        'version': '18.0-230521',
        'components': {
           'msadapt': ['abbd0ffd14624519d2c616613f71190b254fc20b6f5c8efc2ab3b9603f580292', 'base'],
           'gmvoxel': ['5b48674a1dc9aa0e8016c38a3c40d31a8636cf93371f3f6bc9d1ecb4c89d6dc9', 'voxel'],
           'msparalleladapt': ['7e6242387c21b549187a9d985ae91afc0e91f15045a1c961736e53a3f6808e96', 'paralleladapt'],
           'msparallelmesh': ['200db5700e06575408d86e2da9b76fe855182d8284537b18aca2295bbddc97ba', 'parallelmesh'],
           'fdcore': ['dc8c0e222b35ec28cc6c437789f6d8bfa6e4550bb3d3403341530302c1494662', 'base'],
           'discretemodeling': ['9a4bd53d8921c2d8dfae77fdf0f068dfb3fffe0ba4bb19beba72cf38be5eb651', 'discrete'],
           'mscore': ['1ec8b74d709a8325e1d65e831a46ff523f6c1a4912a4405ab57a2ba934fe53c2', 'base'],
           'gmadv': ['170a15f79f00ed81a0aa6b74fa6c38db92ecb186f960af0c1b8f2a4648dd4e85', 'advmodel'],
           'aciskrnl': ['7039e4e05532b689ad7e87a94808fd8d7480c3f53c256e921b76dc601b944976', 'acis'],
           'pskrnl': ['732f3f39aa22a64d1d296572b4c7b579b0612ae55c887ee1c09213ab03f4b4f0', 'parasolid'],
           'gmcore': ['a702be7b1dbc58cf8dfe2b88d03c91e85d3af6838a9029e0d7bb435ef763de26', 'base'],
           'mscrack': ['5dc66c27bd01f310db4531beb893ab1bc30771f75f4eefce540bb9b74a2ad3b0', 'crack'],
           'discrete': ['609d3341fa8075a2e6bd084a5e857719e3b865210e5eedd00734cc1034b1813f', 'discrete'],
           'opencascade': ['2abddb078e5e046aecb3dcf4ca45713150ff2cc802225623704e8ed7fa578295', 'opencascade'],
           'gmabstract': ['c953d436814ce3ce952965ffdec423df8c0cf0ed3a102847ffa47f1de11b483f', 'abstract'],
           'msadv': ['d419c087bbae1e132a075e35153b9771f9666ac930ed2e2d66a195f9d341d747', 'adv'],
        },
        'docs': {
           'MeshSim': ['e8159f9d60d6584bc45c61e0e0cd930ac8aa2c750101a7dcd5762bd0089517a6', 'base'],
           'FieldSim': ['568930bf86437e0597268649b7eaf705afa9b45acae65c40acac26b9b32a5854', 'base'],
           'MeshSimAdvanced': ['cd8396f1717969787e6c1edcf561fa0e97354576d3ad359e9572748525367121', 'adv'],
           'MeshSimCrack': ['dc7b8146c6c85e590b170852a09ef9fc4905132bb61f7cc56e1ddcdb61218372', 'crack'],
           'MeshSimAdapt': ['38da3c72dbd1ddf4b9e129319cb2e719fef18d8d4b098b0b45ad69e1884bd3e5', 'base'],
           'GeomSimAdvanced': ['57c9ff7f07d6ec8d60f0f0bc5653cdb3c439bd6c1c50176ece3eda7d6dcfa41f', 'advmodel'],
           'GeomSimParasolid': ['79fffe3f6f615912d0261dba1aea6109e400faa58f6049865fc5e718ff7d15a9', 'parasolid'],
           'ParallelMeshSimAdapt': ['135cd128aece117b187bc6163a8131ab2b908440a2cc3349d7a60c7669147929', 'paralleladapt'],
           'ParallelMeshSim': ['a2855b7a4a6a70517f84e30805dfe7f68dd955fcb069ed61224c584243802bba', 'parallelmesh'],
           'GeomSimGranite': ['a0815b3fd854081f3ed9eba340454faa213477a589e82b1f85dda3d9f3e77f01', 'granite'],
           'GeomSimVoxel': ['aa625e90754b99e55fcbe1831f5372c0a16ec380f413f9f5fca728109a7b131d', 'voxel'],
           'GeomSimDiscreteModeling': ['e799d6421069e8ef0874240b23dfe74b842f89ae1d9e0c8f952cbb30a742895d', 'discrete'],
           'GeomSimDiscrete': ['297ffc6c47e950b923502b0776755e7b60a318d7a0696372fb8161a764c8bc69', 'discrete'],
           'GeomSim': ['8fe9dfa2dd96a453cec11286d2f28b963745065167998cd96bd26b0fefb6c3f0', 'base'],
           'GeomSimAcis': ['08d80352c8afe61771a37d0a40aaebc2991fb7e9d9b6363d728938fb6b204ea8', 'acis'],
           'GeomSimOpenCascade': ['f750f9b201a7287dfdcaa88c810366a5337deacd05284eea1ae0d3c5ff4b07c5', 'opencascade'],
           'GeomSimAbstract': ['3c90f30bb24a82e36654c3128dbf138de7eb7d35377395ba9117cbb79553af6b', 'abstract'],
        }
    },
    {
        "version": "16.0-220312",
        "components": {
            "msparalleladapt": [
                "cc6d6ecba8183f3444e55977af879b297977ff94dd7f6197028110f7e24ea60b",
                "paralleladapt",
            ],
            "msadapt": [
                "ec4a985f9b29914411d299fecfb1a994224070480be5de5f701d9968ba9da9e5",
                "base",
            ],
            "opencascade": [
                "008e7232ee3531b70143129e5a664f7db0e232bad9d11d693d725d39986a8aa4",
                "opencascade",
            ],
            "gmvoxel": [
                "4a74c54c31e9eb93f9a0c09ef3ac88f365efb19666240374aa6d1142db993a2c",
                "voxel",
            ],
            "msadv": ["d33b591147152383130cc2190f1bd7726cb9ea3590468691db3be5815802d888", "adv"],
            "pskrnl": [
                "e154c22c01ecab2e041cf5d87fcb23eab074449dae7f677f17e7863b6da70fdc",
                "parasolid",
            ],
            "gmcore": ["d9ed89d07d83f2c23eca6a27fd9000fd4c8eeefa70ac860aa28a40000a6ec93e", "base"],
            "psint": [
                "5c236e429f28a36a36cb09ec3f4778dc7b6e72447014b684792eea733bb21fd5",
                "parasolid",
            ],
            "msparallelmesh": [
                "a791f4464da54faafdc63dbcaf3d326ffc49c9ea8d53e36cc57c15607cf72db9",
                "parallelmesh",
            ],
            "mscore": ["48e367e476a03a9fa5389830a6c60824b5d620d04d87392e423a33a331ba3595", "base"],
            "fdcore": ["022de14021434d90daee8ea1200c024d98a7eb01bb9cb5a06a3b2f7ffee9c0a1", "base"],
            "gmadv": [
                "6232ec08ef5cff4269d066b035490f33c199fb545355836ef1536b1a00179b2c",
                "advmodel",
            ],
            "gmabstract": [
                "08a6c7423ed59361c5330dbe00b8914d1d55160de73002e7e552c45c8316f37a",
                "abstract",
            ],
            "discrete": [
                "f5ae00688cf202e75686955185d95952e7b581b414dd52bfef0d917e5959ab22",
                "discrete",
            ],
            "aciskrnl": [
                "c2c7b0c495d47a5662765f1b0c6f52863032e63384d85241e6313c4b773e9ed2",
                "acis",
            ],
        },
        "docs": {
            "GeomSimParasolid": [
                "3420fcc1ac67cff8f46b79553cfe478f34676b9b0cd1fa913255b48cbdfd6ad4",
                "parasolid",
            ],
            "GeomSimAcis": [
                "77b31bfb368f1e7981b3a81087e4e287c560e0a0cd08920b36dc81fea25bcdfa",
                "acis",
            ],
            "MeshSimAdvanced": [
                "abeeb0cb10cf3074295a880412e0568b653f2784b1de19f0f8ede5eec536a8bd",
                "adv",
            ],
            "GeomSim": [
                "b1e762111eb8025b966b0aca4bef3768325d9f1c1e3c72a1246b59539e444eb2",
                "base",
            ],
            "GeomSimVoxel": [
                "bc43f931670657a2cae79f9a2a02048b511fa6e405f15e583631e9f6888e7000",
                "voxel",
            ],
            "ParallelMeshSimAdapt": [
                "dd3a0fd6b889dadb45f9a894f684353fffa25bf15be60ae8e09d0c035045e192",
                "paralleladapt",
            ],
            "GeomSimAdvanced": [
                "3e971ae069baf94b38794318f97f16dc25cf50f6a81413903fbe17407cbd73b3",
                "advmodel",
            ],
            "GeomSimGranite": [
                "e438c19bb94a182068bf327988bd1ff9c1e391876cd9b7c74760b98cbfd08763",
                "granite",
            ],
            "FieldSim": [
                "5ede572cbb7539921482390e5890daa92399a5f1ee68a98d3241a7d062667d9d",
                "base",
            ],
            "MeshSimAdapt": [
                "c4be287da651c68e246034b28e141143d83fc3986fd680174a0d6de7b1cc35ab",
                "base",
            ],
            "GeomSimOpenCascade": [
                "34a8d628d07ab66159d6151276e93fdabfcc92a370f5927b66a71d3a8545652c",
                "opencascade",
            ],
            "GeomSimDiscrete": [
                "d2b11367334401ec57390a658715e91bbf3e3a0e8521fab1ad5d3f7c215b2921",
                "discrete",
            ],
            "GeomSimAbstract": [
                "601b0179b65a385a39d241a9a4e3074e4f834c817e836bea07516015c769e666",
                "abstract",
            ],
            "GeomSimDiscreteModeling": [
                "619b8254d8e3bcc94e84551e997b577dd9325131d084c3b3693ab665b7e4213b",
                "discrete",
            ],
            "ParallelMeshSim": [
                "5b74b9b5f9290111366e341c12d4777635e375523d42cb0a2b24aa1bfa8ab8c4",
                "parallelmesh",
            ],
            "MeshSim": [
                "2f1944e1853a550cc474201790555212e4b7a21d3675715de416718a789ccae2",
                "base",
            ],
        },
    },
    {
        "version": "16.0-210623",
        "components": {
            "gmadv": [
                "c40dac44695db6e97c4d4c06d1eb6eac93518c93d7860c77a69f3ea30fea3b90",
                "advmodel",
            ],
            "msparallelmesh": [
                "57d710b74887731ea0e664a154489747033af433852809181c11e8065752eaf4",
                "parallelmesh",
            ],
            "gmcore": ["5bd04f175fdf5a088140af5ca3fa03934251c097044b47fdf3ea2cd0afc28547", "base"],
            "pskrnl": [
                "87957818b20839d3835a343894c396f7c591d1f0bfd728d33ad21b1adb4e887c",
                "parasolid",
            ],
            "msadapt": [
                "5ba66819bb2c56eb1e07e6c2659afc8c971005b08ed059f8c62a185236e45dac",
                "base",
            ],
            "gmvoxel": [
                "15dfc389665086ea37b9835fecd6b46070572878308796afa960077cc2bf7e0a",
                "voxel",
            ],
            "msparalleladapt": [
                "1db2c34a398c5965a2a675006c96a3603e0124188b52159776b7c616efa48457",
                "paralleladapt",
            ],
            "mscore": ["7029871c52d6c3bb782ae2acb7360130105649cd9cf63815ae95cf4089cb786d", "base"],
            "psint": [
                "c8a3dbacafa70b13bc9fb8322699a1cfc812b2cfd3ea05cba9135623eae761d8",
                "parasolid",
            ],
            "fdcore": ["75f9bcd7cb9ab9dedb73166539c08b53bd8e91c5619d3dce605ba19c63d1ee5c", "base"],
            "msadv": ["0018e0a6b9d7724867f7379bc619269481c318ee4dfd0724511c032534ae04a1", "adv"],
            "aciskrnl": [
                "2a9b9da9b0c09857de7fef0dea0e96222bd30e297bd37bea962751dab6762500",
                "acis",
            ],
            "discrete": [
                "f17cd198f8749c763cc8e200cfd6734604e1d316a48d7d0e537a9a890d884904",
                "discrete",
            ],
            "gmabstract": [
                "068d0309d5ff9668fc0474edf7f4e20503827400e34492e2ed55b46a0c9e1858",
                "abstract",
            ],
        },
        "docs": {
            "GeomSimAdvanced": [
                "02e4566042ae4de10c4acb577142e82d15f32caa296fe1b578c62a38da707066",
                "advmodel",
            ],
            "MeshSim": [
                "cc1dc77cece7aac6ded003c872c651ad8321bc9ce931ad141b17d2de7bf513c5",
                "base",
            ],
            "GeomSimVoxel": [
                "49b8f85f59acc8c973bf46c1f999a0ae64cdf129371587879de056c0ac3500d8",
                "voxel",
            ],
            "MeshSimAdvanced": [
                "2d2689979104414d91d804ca3c34a69104e572b8f231c4e324b09e57675b61cc",
                "adv",
            ],
            "GeomSimGranite": [
                "17f18831a12b06c0e085486d94d3a4275d7ed94ad53fec689e8877217856c750",
                "granite",
            ],
            "GeomSimParasolid": [
                "492bd311cc42dadd1f76064c57d35e886b9a7da4c48576ec4d34844fcdaddb8d",
                "parasolid",
            ],
            "GeomSimAcis": [
                "341c6aeda7f9189f4e886cb75c5989cb9ece6ecba1b1c9d5273b94f74a3dd40b",
                "acis",
            ],
            "GeomSimDiscrete": [
                "e9d42da613a3acadbcdee5d8d6fc3b093f58b51d158f2a392b7da0e5f74e0388",
                "discrete",
            ],
            "MeshSimAdapt": [
                "e27510e588105bdb0ca62c2629dfd41dfca6039b7b2ff0298ef83d3a48d7dd23",
                "base",
            ],
            "GeomSimAbstract": [
                "398c1a15efcddd3b86a7b0334af6f8b529710f815f73f5655d3c7271e92b194e",
                "abstract",
            ],
            "GeomSimDiscreteModeling": [
                "f444aed59569731f65eea920322adcc224c67b715ecba85a1898cf418de58237",
                "discrete",
            ],
            "FieldSim": [
                "bac947998d4de1c4edba271645310d4784290bec30bf0cf41d00ae6ea8b27c97",
                "base",
            ],
            "GeomSim": [
                "95cb24165d47701daa8da7131ca1173d38f4dab80c1ca0d75843b464fed92097",
                "base",
            ],
            "ParallelMeshSim": [
                "fb1e3ac0ab7208d771057880c693e529e7c821772265b89125d371a1b34fa651",
                "parallelmesh",
            ],
            "ParallelMeshSimAdapt": [
                "246c5c8b30194239f41a79f2ffd205fd9ae69bcb8127d19a94f12c278a27f106",
                "paralleladapt",
            ],
        },
    },
    {
        "version": "14.0-191122",
        "components": {
            "gmadv": [
                "01cea5f7aff5e442ea544df054969740ad33e2ff4097cf02de31874d16a0c7c2",
                "advmodel",
            ],
            "msadapt": [
                "69839698f24969f97963869fd212bdcff0b5d52dd40ec3fdc710d878e43b527a",
                "base",
            ],
            "gmvoxel": [
                "bfea15e1fc5d258ed9db69132042a848ca81995e92bf265215e4b88d08a308a8",
                "voxel",
            ],
            "gmabstract": [
                "dccdcd4b71758e4110cd69b0befa7875e5c1f3871f87478410c6676da3f39092",
                "abstract",
            ],
            "fdcore": ["6981b2eb0c0143e6abc3ec29918fc3552f81018755770bf922d2491275984e1a", "base"],
            "msparallelmesh": [
                "1e1a431ec9dd85354ff42c6a2a41df7fbe3dfe5d296f40105c4d3aa372639dc3",
                "parallelmesh",
            ],
            "mscore": ["bca80fcb2c86e7b6dc0259681ccd73197ce85c47f00f1910bd6b518fa0b3a092", "base"],
            "discrete": [
                "430e5f2270864b1ab9c8dff75d2510147a0c5cde8af0828975d9e38661be3a35",
                "discrete",
            ],
            "gmimport": [
                "e83b3c43b7c695fa96ed42253a4b317a2882bcb8987fd3225c09492e353e49aa",
                "import",
            ],
            "pskrnl": [
                "31455cfce746b2339b3644f3890d4444014fb839654a9f576ec747d28ff6c1c4",
                "parasolid",
            ],
            "gmcore": ["af5d89b9ce266cac5b45f2bf96e1324e87e54c6e2f568bd5b6a85c41122d39e4", "base"],
            "aciskrnl": [
                "764e5633e6d502951788accfb8c34ed59430a4779a44d1775fd67f9aab8a654a",
                "acis",
            ],
            "msparalleladapt": [
                "8ae607112958f6b9d319736c71a6597cf99a8a59ceed733f2a939cb9cfa6dd67",
                "paralleladapt",
            ],
            "psint": [
                "f6c90b2fe87e690b2cba20f357d03c5962fed91541d6b79e01dc25cb8f01d1e0",
                "parasolid",
            ],
            "msadv": ["f18a8285d539cb07b00fde06fe970d958eceabf2a10182bcca6c8ad1c074c395", "adv"],
        },
        "docs": {
            "MeshSim": [
                "f3c475072f270ff49ac2f6639ca1cddb0642889648cbea7df1a3f1b85f7cac36",
                "base",
            ],
            "GeomSimVoxel": [
                "9f4ee5a8204fee1d899cb912e0379f8be7a826e81ca0a0d8a670a4b804ca1276",
                "voxel",
            ],
            "MeshSimAdvanced": [
                "8c8bc3709238e600e8938c7c345588f8947d89eae98a228b0d0e3d46f5f4c0d9",
                "adv",
            ],
            "GeomSimDiscreteModeling": [
                "4e8e26a88e8a5ad396a637597a52f5973d8f77abc0a5b99fa737caf37226d6cc",
                "discrete",
            ],
            "GeomSimAdvanced": [
                "5efb38317d6be7862ce34024922ca372b30691a30af820474e2e26e4c3055278",
                "advmodel",
            ],
            "GeomSimParasolid": [
                "6851bdaf6d96e7b2335fce3394825e9876800f0aba0a42644758dc1bd06f60fe",
                "parasolid",
            ],
            "GeomSimImport": [
                "d931ecfc332460c825b473c0950c7ae8ff9f845e0d1565f85bfd7698da5e6d26",
                "import",
            ],
            "ParallelMeshSim": [
                "0f0d235b25a660271e401488e412220f574b341dadb827f7b82f0e93172b5cdb",
                "parallelmesh",
            ],
            "ParallelMeshSimAdapt": [
                "7964ebbd7e8d971ea85fc5260e44f7e876da5ad474dc67d8d6fc939bfa5ba454",
                "paralleladapt",
            ],
            "GeomSimAcis": [
                "dea82efbc4e3043ecda163be792ef295057e08be17654a7783ce7ca5e786f950",
                "acis",
            ],
            "MeshSimAdapt": [
                "ee4d5595572c1fe1a0d78bd9b85c774a55e994c48170450d6c5f34b05fcf2411",
                "base",
            ],
            "FieldSim": [
                "6b09b4ab278911d3e9229fd4cd8dc92ba188f151d42d9d7b96d542aad2af1fac",
                "base",
            ],
            "GeomSim": [
                "0673823d649998367c0e427055911eae971bb6e8c76625882e7a7901f4d18c44",
                "base",
            ],
            "GeomSimDiscrete": [
                "58dfd33fc5cdd2ab24e9084377943f28d5ba68b8c017b11b71cde64c5e4f2113",
                "discrete",
            ],
            "GeomSimAbstract": [
                "16248cd2a0d133029eb4b79d61397da008e4d5b5c3eaf0161a0a44148b0bc519",
                "abstract",
            ],
        },
    },
    {
        "version": "12.0-191027",
        "components": {
            "gmadv": [
                "1a133523062974c4d9acb1d52baa3893dc891482aebaaeb79a7dc907461d5dbc",
                "advmodel",
            ],
            "fdcore": ["c3a89093f811cb489698d203dbe68ca910e6c67ea75c0a7aba73dd369508b9ec", "base"],
            "mscore": ["a2f043278d45d8729020b663c66c57960fcec33dafd3d90db55f0a9e32723bce", "base"],
            "msparallelmesh": [
                "2f6fd47d3c5c2f1ece4634985a522ac599d3cee20ad8a4623f252cc75aa32c4c",
                "parallelmesh",
            ],
            "msparalleladapt": [
                "8d288730b1300215a32f3b21624bd2e0e2d8a684fe928459757fcec7e0aeb7d3",
                "paralleladapt",
            ],
            "gmabstract": [
                "3b608f21e6c11db5bb48e49f9cd7e9d88aeec4feadebd778529a5c9d506d08c6",
                "abstract",
            ],
            "gmimport": [
                "fc1626c7b1522b90eaa3926e1253b84d28440c7df8634decdedb79b5229be800",
                "import",
            ],
            "discrete": [
                "a15ead08138f0c59c7ee46cd0d348d4f26e1b021d2580a134cf2b84a7337bcf9",
                "discrete",
            ],
            "aciskrnl": [
                "8773f00e08d237052c877e79d1a869214f59891e812d70df938b2a5e5423a96f",
                "acis",
            ],
            "msadv": ["41bdb9555ab9feb0891f0832a49fc29777d40957473f315e1c33e1c0077cba7d", "adv"],
            "psint": [
                "b040ab48833eb2a748f757e2de6929f3002aa98db459ba92bd9a88e443e5cb07",
                "parasolid",
            ],
            "gmvoxel": [
                "19fba83c9c7eac20d9613236530fbae652dc8edef35233214f0f92b81c91a877",
                "voxel",
            ],
            "msadapt": [
                "1a752adb6724c3328fffb26f1aebed007d3c2a5df725cd29aa0cf0fdfda1f39a",
                "base",
            ],
            "gmcore": ["ec95bae84b36644e6e04cf0a6b4e813a51990d0a30519176ebb8a05f681af7f2", "base"],
            "pskrnl": [
                "7b7b4952513e06c8c23aa8f7c1748f5c199d9af70ea06c4a359412237ed8ac1d",
                "parasolid",
            ],
        },
        "docs": {
            "FieldSim": [
                "5109d91fe61ccdaf0af5aa869aea9c38ec98760746ec3983d100f870cbb1cb63",
                "base",
            ],
            "ParallelMeshSim": [
                "a1e6618a77022a9580beac4c698dd4b9aa70f617a27db9ce13ab1f2388475290",
                "parallelmesh",
            ],
            "GeomSimAcis": [
                "f0319b32eb417fa9b237575d9b2dc1c061848888c36fd4da97d97cdbb3cf19c3",
                "acis",
            ],
            "GeomSimAbstract": [
                "c44023e6944522057c47925db49089031c7de9b67938ca6a987e04fadfeda9b7",
                "abstract",
            ],
            "GeomSimDiscrete": [
                "ad648752fa7d2dc1ce234a612e28ce84eb1f064a1decadf17b42e9fe56967350",
                "discrete",
            ],
            "MeshSimAdapt": [
                "dcb7d6ec74c910b41b5ae707d9fd4664fcb3a0fdb2c876caaa28a6f1cf701024",
                "base",
            ],
            "MeshSim": [
                "e5a8cb300b1e13b9f2733bf8b738872ffb37d9df15836a6ab264483c10000696",
                "base",
            ],
            "GeomSimParasolid": [
                "2bf33cc5b3879716437d45fde0a02caaa165e37d248d05b4b00708e76573a15e",
                "parasolid",
            ],
            "GeomSimImport": [
                "5309433dcdce660e062412f070719eefcc6299764e9b0169533ff343c9c9c406",
                "import",
            ],
            "ParallelMeshSimAdapt": [
                "2e8e0ceede3107b85dba9536f3bbf5e6959793073a5147548cfb01ca568c8da2",
                "paralleladapt",
            ],
            "GeomSimDiscreteModeling": [
                "ff88ec234b890315cc36539e3f73f4f977dab94160860950e7b7ee0303c9b55e",
                "discrete",
            ],
            "GeomSim": [
                "62ae33372f999d5e62a1b7b161ddd7de04c055adc85cfd258e088c95b76d5fef",
                "base",
            ],
            "GeomSimVoxel": [
                "7a624ddaebd833077511acac3efd4b4c1dab09bd9feff40aba0813182eeb262f",
                "voxel",
            ],
            "GeomSimAdvanced": [
                "f0ab801ddf3d701a4ac3f8c47900cc858a4488eb0fe2f663504ba260cd270d20",
                "advmodel",
            ],
            "MeshSimAdvanced": [
                "bb532027e4fcc311a7c376383da010aed5ee133a9122b186a4e5c7d0cf1d976b",
                "adv",
            ],
        },
    },
]


def simmetrix_makecomponenturl(name):
    """only supporting the linux libraries"""
    prefix = "file://{0}/".format(os.getcwd())
    suffix = "-" + "linux64.tgz"
    return prefix + name + suffix


def simmetrix_makedocurl(name):
    """doc zip files are not os/arch specific"""
    prefix = "file://{0}/".format(os.getcwd())
    suffix = ".zip"
    return prefix + name + suffix


def simmetrix_setkernelcmakeprefixpath(spec, path, env):
    if "+acis" in spec:
        env.append_path("CMAKE_PREFIX_PATH", join_path(path, "acisKrnl"))
        env.append_path("LD_LIBRARY_PATH", join_path(path, "acisKrnl"))
    if "+parasolid" in spec:
        env.append_path("CMAKE_PREFIX_PATH", join_path(path, "psKrnl"))
        env.append_path("LD_LIBRARY_PATH", join_path(path, "psKrnl"))


def simmetrix_resource(name, url, sha256, condition):
    # The tarballs/zips each have the same directory structure.  Because of
    # this, and the bug in spack described here:
    # https://github.com/spack/spack/pull/3553#issuecomment-391424244
    # , they cannot be expanded into the source root directory.
    # Once this is fixed the 'destination=name' argument can be removed.
    resource(name=name, url=url, sha256=sha256, destination=name, when=condition)


class SimmetrixSimmodsuite(Package):
    """Simmetrix' Simulation Modeling Suite is a set of component software
    toolkits that allow developers to easily implement geometry-based
    simulation applications.
    Each component of the Simulation Modeling Suite is designed to address
    specific capabilities:
    | MeshSim - automatic mesh generation
    | FieldSim - simulation data management
    | GeomSim - direct, untranslated access to geometry from a wide variety
    of sources
    """

    maintainers("cwsmith")
    homepage = "http://www.simmetrix.com/products/SimulationModelingSuite/main.html"
    manual_download = True

    license_required = True
    license_vars = ["SIM_LICENSE_FILE"]

    variant("base", default=True, description="enable the base components")
    variant("advmodel", default=False, description="enable advaced modeling")
    variant("abstract", default=False, description="enable abstract modeling")
    variant("voxel", default=False, description="enable voxel modeling")
    variant("discrete", default=False, description="enable discrete modeling")
    variant("acis", default=False, description="enable acis modeling")
    variant("parasolid", default=False, description="enable parasolid modeling")
    variant(
        "opencascade",
        default=False,
        when="@16.0-220312:",
        description="enable opencascade modeling",
    )
    variant("granite", default=False, description="enable granite modeling")
    variant("import", default=False, description="enable import modeling")
    variant("adv", default=False, description="enable advanced meshing")
    variant("parallelmesh", default=False, description="enable parallel meshing")
    variant("paralleladapt", default=False, description="enable parallel adaptation")
    variant(
        "octree",
        default=False,
        when="@2023.0-240303:",
        description="enable octree based discretization functionality",
    )


    depends_on("mpi")
    depends_on("libtirpc", type="link")
    depends_on("cxx", type="link")
    depends_on("gmake")

    oslib = "x64_rhel8_gcc83"

    for release in RELEASES:
        # define the version using the mscore tarball
        sim_version = release["version"]
        main_pkg_name = "mscore"
        url = simmetrix_makecomponenturl(main_pkg_name)
        sha256 = release["components"][main_pkg_name][0]
        version(sim_version, sha256=sha256, url=url)
        # define resources for the other tarballs
        for _name, atts in release["components"].items():
            # skip the tarball used for the version(...) call
            if _name == "mscore":
                continue
            sha256 = atts[0]
            feature = atts[1]
            url = simmetrix_makecomponenturl(_name)
            condition = "@{0}+{1}".format(sim_version, feature)
            simmetrix_resource(_name, url, sha256, condition)
        # define resources for the document zip files
        for _name, atts in release["docs"].items():
            sha256 = atts[0]
            feature = atts[1]
            url = simmetrix_makedocurl(_name)
            condition = "@{0}+{1}".format(sim_version, feature)
            simmetrix_resource(_name, url, sha256, condition)

    def setup_dependent_build_environment(self, env, dependent_spec):
        archlib = join_path(self.prefix.lib, self.oslib)
        env.append_path("CMAKE_PREFIX_PATH", archlib)
        simmetrix_setkernelcmakeprefixpath(self.spec, archlib, env)

    def setup_run_environment(self, env):
        archlib = join_path(self.prefix.lib, self.oslib)
        env.append_path("CMAKE_PREFIX_PATH", archlib)
        simmetrix_setkernelcmakeprefixpath(self.spec, archlib, env)

    def install(self, spec, prefix):
        if not spec.satisfies("platform=linux"):
            raise InstallError("Only the linux platform is supported")
        source_path = self.stage.source_path
        for release in RELEASES:
            simversion = release["version"]
            if simversion != spec.version.string:
                continue
            for name, atts in release["components"].items():
                feature = atts[1]
                if "+" + feature in spec:
                    if name == "mscore":
                        install_tree(join_path(source_path, "lib"), prefix.lib)
                        install_tree(join_path(source_path, "include"), prefix.include)
                    else:
                        path = join_path(source_path, name, self.version.string)
                        install_tree(path, prefix)
            for name, atts in release["docs"].items():
                feature = atts[1]
                if "+" + feature in spec:
                    path = join_path(source_path, name, self.version.string)
                    install_tree(path, prefix)

        workdir = prefix.code.PartitionWrapper
        if "+parallelmesh" in spec:
            with working_dir(workdir):
                mpi_id = spec["mpi"].name + spec["mpi"].version.string
                # build the wrapper lib
                make(
                    "-f",
                    "Makefile.custom",
                    "CC=%s" % spec["mpi"].mpicc,
                    "CXX=%s" % spec["mpi"].mpicxx,
                    "PARALLEL=%s" % mpi_id,
                    "PQUAL=-%s" % mpi_id,
                    "OPTFLAGS=-O2 -DNDEBUG " + self['cxx'].pic_flag,
                )
                libname = "libSimPartitionWrapper-" + mpi_id + ".a"
                wrapperlibpath = join_path(workdir, "lib", libname)
                install(wrapperlibpath, join_path(prefix.lib, self.oslib))
