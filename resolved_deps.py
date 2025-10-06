resolved = [
     {
          "original_rule_class": "local_config_platform",
          "original_attributes": {
               "name": "local_config_platform"
          },
          "native": "local_config_platform(name = 'local_config_platform')"
     },
     {
          "original_rule_class": "local_repository",
          "original_attributes": {
               "name": "bazel_tools",
               "path": "C:/Users/Gebruiker/_bazel_Gebruiker/install/df1e8724e64eb8d90c9b2cd66e1f2404/embedded_tools"
          },
          "native": "local_repository(name = \"bazel_tools\", path = __embedded_dir__ + \"/\" + \"embedded_tools\")"
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository googleapis+ instantiated at:\n  <builtin>: in <toplevel>\nRepository rule http_archive defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/bazel_tools/tools/build_defs/repo/http.bzl:431:31: in <toplevel>\n",
          "original_attributes": {
               "name": "googleapis+",
               "urls": [
                    "https://github.com/googleapis/googleapis/archive/a92cee399e0fc8afa2d460373b1085f543bc8d3f.zip"
               ],
               "integrity": "sha256-Od5IoRLQ+/+AOkj877bFFU+cWj/n2toEHDX6JDRvevg=",
               "strip_prefix": "googleapis-a92cee399e0fc8afa2d460373b1085f543bc8d3f",
               "remote_file_urls": {
                    "MODULE.bazel": [
                         "https://bcr.bazel.build/modules/googleapis/0.0.0-20250826-a92cee39/overlay/MODULE.bazel"
                    ],
                    "extensions.bzl": [
                         "https://bcr.bazel.build/modules/googleapis/0.0.0-20250826-a92cee39/overlay/extensions.bzl"
                    ],
                    "tests/bcr/.bazelrc": [
                         "https://bcr.bazel.build/modules/googleapis/0.0.0-20250826-a92cee39/overlay/tests/bcr/.bazelrc"
                    ],
                    "tests/bcr/BUILD.bazel": [
                         "https://bcr.bazel.build/modules/googleapis/0.0.0-20250826-a92cee39/overlay/tests/bcr/BUILD.bazel"
                    ],
                    "tests/bcr/MODULE.bazel": [
                         "https://bcr.bazel.build/modules/googleapis/0.0.0-20250826-a92cee39/overlay/tests/bcr/MODULE.bazel"
                    ],
                    "tests/bcr/failure_test.bzl": [
                         "https://bcr.bazel.build/modules/googleapis/0.0.0-20250826-a92cee39/overlay/tests/bcr/failure_test.bzl"
                    ]
               },
               "remote_file_integrity": {
                    "MODULE.bazel": "sha256-HyQ3XSTI6RyJD3moHFReFcbPSkGLvoL0L3nrSFd68r8=",
                    "extensions.bzl": "sha256-59FkoqrMX/a/7t3zkSLDmMkuGnajSeOoZI4FZFIwEuw=",
                    "tests/bcr/.bazelrc": "sha256-hFZT+gits3VtXcUkKuh3NCEC9FgBNGuNxaOVCuOiFPk=",
                    "tests/bcr/BUILD.bazel": "sha256-KZzDURLUNDOiMsurUHrnuWYogHPFs7W+Ar9ZrilPLuE=",
                    "tests/bcr/MODULE.bazel": "sha256-4zmBG1uAn7W3ExjUMQChBcrJVSNCE6K8PhIs9SfKy1U=",
                    "tests/bcr/failure_test.bzl": "sha256-AJLzf7NfQOLpWbNIR3TIU28tQMSjd3svlAgh4yCoXm8="
               },
               "remote_module_file_urls": [
                    "https://bcr.bazel.build/modules/googleapis/0.0.0-20250826-a92cee39/MODULE.bazel"
               ],
               "remote_module_file_integrity": "sha256-HyQ3XSTI6RyJD3moHFReFcbPSkGLvoL0L3nrSFd68r8=",
               "remote_patches": {
                    "https://bcr.bazel.build/modules/googleapis/0.0.0-20250826-a92cee39/patches/module_dot_bazel.patch": "sha256-d3qQKa30fFxPBkGfx6C85GR9d76i9M8lK2qO9jlVCTc=",
                    "https://bcr.bazel.build/modules/googleapis/0.0.0-20250826-a92cee39/patches/remove_upb_c_rules.patch": "sha256-MmXB+YzXhG05hDbVgw5S/VZRgu4b2qjQl0OHVEEtP7Y="
               },
               "remote_patch_strip": 0
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "name": "googleapis+",
                         "urls": [
                              "https://github.com/googleapis/googleapis/archive/a92cee399e0fc8afa2d460373b1085f543bc8d3f.zip"
                         ],
                         "integrity": "sha256-Od5IoRLQ+/+AOkj877bFFU+cWj/n2toEHDX6JDRvevg=",
                         "strip_prefix": "googleapis-a92cee399e0fc8afa2d460373b1085f543bc8d3f",
                         "remote_file_urls": {
                              "MODULE.bazel": [
                                   "https://bcr.bazel.build/modules/googleapis/0.0.0-20250826-a92cee39/overlay/MODULE.bazel"
                              ],
                              "extensions.bzl": [
                                   "https://bcr.bazel.build/modules/googleapis/0.0.0-20250826-a92cee39/overlay/extensions.bzl"
                              ],
                              "tests/bcr/.bazelrc": [
                                   "https://bcr.bazel.build/modules/googleapis/0.0.0-20250826-a92cee39/overlay/tests/bcr/.bazelrc"
                              ],
                              "tests/bcr/BUILD.bazel": [
                                   "https://bcr.bazel.build/modules/googleapis/0.0.0-20250826-a92cee39/overlay/tests/bcr/BUILD.bazel"
                              ],
                              "tests/bcr/MODULE.bazel": [
                                   "https://bcr.bazel.build/modules/googleapis/0.0.0-20250826-a92cee39/overlay/tests/bcr/MODULE.bazel"
                              ],
                              "tests/bcr/failure_test.bzl": [
                                   "https://bcr.bazel.build/modules/googleapis/0.0.0-20250826-a92cee39/overlay/tests/bcr/failure_test.bzl"
                              ]
                         },
                         "remote_file_integrity": {
                              "MODULE.bazel": "sha256-HyQ3XSTI6RyJD3moHFReFcbPSkGLvoL0L3nrSFd68r8=",
                              "extensions.bzl": "sha256-59FkoqrMX/a/7t3zkSLDmMkuGnajSeOoZI4FZFIwEuw=",
                              "tests/bcr/.bazelrc": "sha256-hFZT+gits3VtXcUkKuh3NCEC9FgBNGuNxaOVCuOiFPk=",
                              "tests/bcr/BUILD.bazel": "sha256-KZzDURLUNDOiMsurUHrnuWYogHPFs7W+Ar9ZrilPLuE=",
                              "tests/bcr/MODULE.bazel": "sha256-4zmBG1uAn7W3ExjUMQChBcrJVSNCE6K8PhIs9SfKy1U=",
                              "tests/bcr/failure_test.bzl": "sha256-AJLzf7NfQOLpWbNIR3TIU28tQMSjd3svlAgh4yCoXm8="
                         },
                         "remote_module_file_urls": [
                              "https://bcr.bazel.build/modules/googleapis/0.0.0-20250826-a92cee39/MODULE.bazel"
                         ],
                         "remote_module_file_integrity": "sha256-HyQ3XSTI6RyJD3moHFReFcbPSkGLvoL0L3nrSFd68r8=",
                         "remote_patches": {
                              "https://bcr.bazel.build/modules/googleapis/0.0.0-20250826-a92cee39/patches/module_dot_bazel.patch": "sha256-d3qQKa30fFxPBkGfx6C85GR9d76i9M8lK2qO9jlVCTc=",
                              "https://bcr.bazel.build/modules/googleapis/0.0.0-20250826-a92cee39/patches/remove_upb_c_rules.patch": "sha256-MmXB+YzXhG05hDbVgw5S/VZRgu4b2qjQl0OHVEEtP7Y="
                         },
                         "remote_patch_strip": 0
                    },
                    "output_tree_hash": "3da8c78d99e04779eaf8315705c8f56d439b7da20577788b32dac276374541f7"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository rules_shell+ instantiated at:\n  <builtin>: in <toplevel>\nRepository rule http_archive defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/bazel_tools/tools/build_defs/repo/http.bzl:431:31: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_shell+",
               "urls": [
                    "https://github.com/bazelbuild/rules_shell/releases/download/v0.3.0/rules_shell-v0.3.0.tar.gz"
               ],
               "integrity": "sha256-2M1KOpH8HcaNTH1rZV8J3vEJ9xhkN+P1Cptgq0NqDFM=",
               "strip_prefix": "rules_shell-0.3.0",
               "remote_file_urls": {},
               "remote_file_integrity": {},
               "remote_module_file_urls": [
                    "https://bcr.bazel.build/modules/rules_shell/0.3.0/MODULE.bazel"
               ],
               "remote_module_file_integrity": "sha256-3kQCzRL0zI/aI1T84Xn9sGjAucoewtKxez4hskwak3s=",
               "remote_patches": {
                    "https://bcr.bazel.build/modules/rules_shell/0.3.0/patches/module_dot_bazel_version.patch": "sha256-EmJAIbA/eRUtmeJTyvxoadXCXqGv5+NfMx2LAlAy+2Q="
               },
               "remote_patch_strip": 1
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "name": "rules_shell+",
                         "urls": [
                              "https://github.com/bazelbuild/rules_shell/releases/download/v0.3.0/rules_shell-v0.3.0.tar.gz"
                         ],
                         "integrity": "sha256-2M1KOpH8HcaNTH1rZV8J3vEJ9xhkN+P1Cptgq0NqDFM=",
                         "strip_prefix": "rules_shell-0.3.0",
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_module_file_urls": [
                              "https://bcr.bazel.build/modules/rules_shell/0.3.0/MODULE.bazel"
                         ],
                         "remote_module_file_integrity": "sha256-3kQCzRL0zI/aI1T84Xn9sGjAucoewtKxez4hskwak3s=",
                         "remote_patches": {
                              "https://bcr.bazel.build/modules/rules_shell/0.3.0/patches/module_dot_bazel_version.patch": "sha256-EmJAIbA/eRUtmeJTyvxoadXCXqGv5+NfMx2LAlAy+2Q="
                         },
                         "remote_patch_strip": 1
                    },
                    "output_tree_hash": "3af5b9ae6805afd2d1c17bbc0e6097c57096661a4228702da885fec28ebe9cfd"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository rules_java+ instantiated at:\n  <builtin>: in <toplevel>\nRepository rule http_archive defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/bazel_tools/tools/build_defs/repo/http.bzl:431:31: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_java+",
               "urls": [
                    "https://github.com/bazelbuild/rules_java/releases/download/8.14.0/rules_java-8.14.0.tar.gz"
               ],
               "integrity": "sha256-u+fZQ2DMntRgfsX9lJlf0exB6EJXAgtvCeZAVSgeyxI=",
               "strip_prefix": "",
               "remote_file_urls": {},
               "remote_file_integrity": {},
               "remote_module_file_urls": [
                    "https://bcr.bazel.build/modules/rules_java/8.14.0/MODULE.bazel"
               ],
               "remote_module_file_integrity": "sha256-cXcX7UDMaZlFlqRa7G6ngTXqQ0uEAvuRsAm5FR3WVhU=",
               "remote_patches": {},
               "remote_patch_strip": 0
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "name": "rules_java+",
                         "urls": [
                              "https://github.com/bazelbuild/rules_java/releases/download/8.14.0/rules_java-8.14.0.tar.gz"
                         ],
                         "integrity": "sha256-u+fZQ2DMntRgfsX9lJlf0exB6EJXAgtvCeZAVSgeyxI=",
                         "strip_prefix": "",
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_module_file_urls": [
                              "https://bcr.bazel.build/modules/rules_java/8.14.0/MODULE.bazel"
                         ],
                         "remote_module_file_integrity": "sha256-cXcX7UDMaZlFlqRa7G6ngTXqQ0uEAvuRsAm5FR3WVhU=",
                         "remote_patches": {},
                         "remote_patch_strip": 0
                    },
                    "output_tree_hash": "c005da6330f85a45a1debe3e5929247500fe0c2fba4c9dd2425870336ffc9ab3"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository rules_python+ instantiated at:\n  <builtin>: in <toplevel>\nRepository rule http_archive defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/bazel_tools/tools/build_defs/repo/http.bzl:431:31: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_python+",
               "urls": [
                    "https://github.com/bazel-contrib/rules_python/releases/download/1.4.1/rules_python-1.4.1.tar.gz"
               ],
               "integrity": "sha256-n587MAqSZOTHeZkxLOZjvl3umlbjYaH2/n7GDhvu+aM=",
               "strip_prefix": "rules_python-1.4.1",
               "remote_file_urls": {},
               "remote_file_integrity": {},
               "remote_module_file_urls": [
                    "https://bcr.bazel.build/modules/rules_python/1.4.1/MODULE.bazel"
               ],
               "remote_module_file_integrity": "sha256-iZGtRb3CUBgwHWt+HTYmr8PIr4qvS8BPI9C5nJOLc6Y=",
               "remote_patches": {
                    "https://bcr.bazel.build/modules/rules_python/1.4.1/patches/module_dot_bazel_version.patch": "sha256-jog4iTSLzT5uaLYtQ2JMuD3PDk75GvQ4SxEQaU3cb7o="
               },
               "remote_patch_strip": 1
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "name": "rules_python+",
                         "urls": [
                              "https://github.com/bazel-contrib/rules_python/releases/download/1.4.1/rules_python-1.4.1.tar.gz"
                         ],
                         "integrity": "sha256-n587MAqSZOTHeZkxLOZjvl3umlbjYaH2/n7GDhvu+aM=",
                         "strip_prefix": "rules_python-1.4.1",
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_module_file_urls": [
                              "https://bcr.bazel.build/modules/rules_python/1.4.1/MODULE.bazel"
                         ],
                         "remote_module_file_integrity": "sha256-iZGtRb3CUBgwHWt+HTYmr8PIr4qvS8BPI9C5nJOLc6Y=",
                         "remote_patches": {
                              "https://bcr.bazel.build/modules/rules_python/1.4.1/patches/module_dot_bazel_version.patch": "sha256-jog4iTSLzT5uaLYtQ2JMuD3PDk75GvQ4SxEQaU3cb7o="
                         },
                         "remote_patch_strip": 1
                    },
                    "output_tree_hash": "caafc36dfa2fdd0b177c3aee8e018225585c5e80ae5cca20cca67249a7c3625b"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository protobuf+ instantiated at:\n  <builtin>: in <toplevel>\nRepository rule http_archive defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/bazel_tools/tools/build_defs/repo/http.bzl:431:31: in <toplevel>\n",
          "original_attributes": {
               "name": "protobuf+",
               "urls": [
                    "https://github.com/protocolbuffers/protobuf/releases/download/v31.1/protobuf-31.1.zip"
               ],
               "integrity": "sha256-VU6EfkbHBb/ET7LQrlv3jzQ5X8v9hrp0czi1cO7yZ3E=",
               "strip_prefix": "protobuf-31.1",
               "remote_file_urls": {},
               "remote_file_integrity": {},
               "remote_module_file_urls": [
                    "https://bcr.bazel.build/modules/protobuf/31.1/MODULE.bazel"
               ],
               "remote_module_file_integrity": "sha256-N5o4m7Mwt7jBzfMxzJC/PhPeVhR5mztSzbfG84n2s44=",
               "remote_patches": {},
               "remote_patch_strip": 0
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "name": "protobuf+",
                         "urls": [
                              "https://github.com/protocolbuffers/protobuf/releases/download/v31.1/protobuf-31.1.zip"
                         ],
                         "integrity": "sha256-VU6EfkbHBb/ET7LQrlv3jzQ5X8v9hrp0czi1cO7yZ3E=",
                         "strip_prefix": "protobuf-31.1",
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_module_file_urls": [
                              "https://bcr.bazel.build/modules/protobuf/31.1/MODULE.bazel"
                         ],
                         "remote_module_file_integrity": "sha256-N5o4m7Mwt7jBzfMxzJC/PhPeVhR5mztSzbfG84n2s44=",
                         "remote_patches": {},
                         "remote_patch_strip": 0
                    },
                    "output_tree_hash": "3e9dad533efc18f594cd3924f26c67d6074739608a4a36edb9922cb2b752c5f5"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java+//java:rules_java_deps.bzl%_compatibility_proxy_repo_rule",
          "definition_information": "Repository rules_java++compatibility_proxy+compatibility_proxy instantiated at:\n  <builtin>: in <toplevel>\nRepository rule _compatibility_proxy_repo_rule defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/rules_java+/java/rules_java_deps.bzl:107:49: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_java++compatibility_proxy+compatibility_proxy"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java+//java:rules_java_deps.bzl%_compatibility_proxy_repo_rule",
                    "attributes": {
                         "name": "rules_java++compatibility_proxy+compatibility_proxy"
                    },
                    "output_tree_hash": "ebbbc4825c01582ab216dbce529d9253adc5f4004c5de360474438b104769c7e"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository rules_cc+ instantiated at:\n  <builtin>: in <toplevel>\nRepository rule http_archive defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/bazel_tools/tools/build_defs/repo/http.bzl:431:31: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_cc+",
               "urls": [
                    "https://github.com/bazelbuild/rules_cc/releases/download/0.1.4/rules_cc-0.1.4.tar.gz"
               ],
               "integrity": "sha256-DTtPmExMLhrP0TeOAUjTXK8u8dnrlbaI+OGc4MQb31s=",
               "strip_prefix": "rules_cc-0.1.4",
               "remote_file_urls": {},
               "remote_file_integrity": {},
               "remote_module_file_urls": [
                    "https://bcr.bazel.build/modules/rules_cc/0.1.4/MODULE.bazel"
               ],
               "remote_module_file_integrity": "sha256-uwOkUqdSesJadRj7hqlG72PfhguWV9gyOgxQ+FBPsLk=",
               "remote_patches": {
                    "https://bcr.bazel.build/modules/rules_cc/0.1.4/patches/module_dot_bazel_version.patch": "sha256-PTxaVY2h9V4VtrvTW+N43r+fRdLKKpyeDJcu89+Vr4s="
               },
               "remote_patch_strip": 1
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "name": "rules_cc+",
                         "urls": [
                              "https://github.com/bazelbuild/rules_cc/releases/download/0.1.4/rules_cc-0.1.4.tar.gz"
                         ],
                         "integrity": "sha256-DTtPmExMLhrP0TeOAUjTXK8u8dnrlbaI+OGc4MQb31s=",
                         "strip_prefix": "rules_cc-0.1.4",
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_module_file_urls": [
                              "https://bcr.bazel.build/modules/rules_cc/0.1.4/MODULE.bazel"
                         ],
                         "remote_module_file_integrity": "sha256-uwOkUqdSesJadRj7hqlG72PfhguWV9gyOgxQ+FBPsLk=",
                         "remote_patches": {
                              "https://bcr.bazel.build/modules/rules_cc/0.1.4/patches/module_dot_bazel_version.patch": "sha256-PTxaVY2h9V4VtrvTW+N43r+fRdLKKpyeDJcu89+Vr4s="
                         },
                         "remote_patch_strip": 1
                    },
                    "output_tree_hash": "c7cf3251e3698cfe02d2e9822c0e1cbd70b3fd448d2cef505b530fb666f8bf6b"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository bazel_skylib+ instantiated at:\n  <builtin>: in <toplevel>\nRepository rule http_archive defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/bazel_tools/tools/build_defs/repo/http.bzl:431:31: in <toplevel>\n",
          "original_attributes": {
               "name": "bazel_skylib+",
               "urls": [
                    "https://github.com/bazelbuild/bazel-skylib/releases/download/1.8.1/bazel-skylib-1.8.1.tar.gz"
               ],
               "integrity": "sha256-UbUQWnYLNTdz+QTSu8XmZNCYf7ryImUWTeZdQ+kQ2Kw=",
               "strip_prefix": "",
               "remote_file_urls": {},
               "remote_file_integrity": {},
               "remote_module_file_urls": [
                    "https://bcr.bazel.build/modules/bazel_skylib/1.8.1/MODULE.bazel"
               ],
               "remote_module_file_integrity": "sha256-iK3nKTvs2pY+Dj6jPn1U00JRJ+CjJuDRfaCFpfHwP/Y=",
               "remote_patches": {},
               "remote_patch_strip": 0
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "name": "bazel_skylib+",
                         "urls": [
                              "https://github.com/bazelbuild/bazel-skylib/releases/download/1.8.1/bazel-skylib-1.8.1.tar.gz"
                         ],
                         "integrity": "sha256-UbUQWnYLNTdz+QTSu8XmZNCYf7ryImUWTeZdQ+kQ2Kw=",
                         "strip_prefix": "",
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_module_file_urls": [
                              "https://bcr.bazel.build/modules/bazel_skylib/1.8.1/MODULE.bazel"
                         ],
                         "remote_module_file_integrity": "sha256-iK3nKTvs2pY+Dj6jPn1U00JRJ+CjJuDRfaCFpfHwP/Y=",
                         "remote_patches": {},
                         "remote_patch_strip": 0
                    },
                    "output_tree_hash": "62336cfc5d02b7c9a8097662f62cea03306822925d2078e0c29a9562c10ae92e"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository bazel_features+ instantiated at:\n  <builtin>: in <toplevel>\nRepository rule http_archive defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/bazel_tools/tools/build_defs/repo/http.bzl:431:31: in <toplevel>\n",
          "original_attributes": {
               "name": "bazel_features+",
               "urls": [
                    "https://github.com/bazel-contrib/bazel_features/releases/download/v1.30.0/bazel_features-v1.30.0.tar.gz"
               ],
               "integrity": "sha256-pmACf1qH8TIkq1S43G4ZFpPFVPJpL8ykbo4p7n2rxDs=",
               "strip_prefix": "bazel_features-1.30.0",
               "remote_file_urls": {},
               "remote_file_integrity": {},
               "remote_module_file_urls": [
                    "https://bcr.bazel.build/modules/bazel_features/1.30.0/MODULE.bazel"
               ],
               "remote_module_file_integrity": "sha256-oUti0FlpopO4AlfnLll8Laf3F+Hmn6izOXA+1nMb7Ic=",
               "remote_patches": {
                    "https://bcr.bazel.build/modules/bazel_features/1.30.0/patches/module_dot_bazel_version.patch": "sha256-BSaT4TEsvkWjavZkZ+vYj0I8bzxEEj1s3L9YMr8ylO0="
               },
               "remote_patch_strip": 1
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "name": "bazel_features+",
                         "urls": [
                              "https://github.com/bazel-contrib/bazel_features/releases/download/v1.30.0/bazel_features-v1.30.0.tar.gz"
                         ],
                         "integrity": "sha256-pmACf1qH8TIkq1S43G4ZFpPFVPJpL8ykbo4p7n2rxDs=",
                         "strip_prefix": "bazel_features-1.30.0",
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_module_file_urls": [
                              "https://bcr.bazel.build/modules/bazel_features/1.30.0/MODULE.bazel"
                         ],
                         "remote_module_file_integrity": "sha256-oUti0FlpopO4AlfnLll8Laf3F+Hmn6izOXA+1nMb7Ic=",
                         "remote_patches": {
                              "https://bcr.bazel.build/modules/bazel_features/1.30.0/patches/module_dot_bazel_version.patch": "sha256-BSaT4TEsvkWjavZkZ+vYj0I8bzxEEj1s3L9YMr8ylO0="
                         },
                         "remote_patch_strip": 1
                    },
                    "output_tree_hash": "d7c9a5eaa4b3f71f5e5d84040faaa66ed0f028ed67b5bca48fa9c412067330be"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_python+//python/private:internal_config_repo.bzl%internal_config_repo",
          "definition_information": "Repository rules_python++internal_deps+rules_python_internal instantiated at:\n  <builtin>: in <toplevel>\nRepository rule internal_config_repo defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/rules_python+/python/private/internal_config_repo.bzl:114:39: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_python++internal_deps+rules_python_internal"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_python+//python/private:internal_config_repo.bzl%internal_config_repo",
                    "attributes": {
                         "name": "rules_python++internal_deps+rules_python_internal"
                    },
                    "output_tree_hash": "e1384718ad44e4ffcc46cbf70f35cc8d474012ed34f3ae07298b4f99fc5153f4"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_features+//private:globals_repo.bzl%globals_repo",
          "definition_information": "Repository bazel_features++version_extension+bazel_features_globals instantiated at:\n  <builtin>: in <toplevel>\nRepository rule globals_repo defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/bazel_features+/private/globals_repo.bzl:46:31: in <toplevel>\n",
          "original_attributes": {
               "name": "bazel_features++version_extension+bazel_features_globals",
               "globals": {
                    "CcSharedLibraryInfo": "6.0.0-pre.20220630.1",
                    "CcSharedLibraryHintInfo": "7.0.0-pre.20230316.2",
                    "macro": "8.0.0",
                    "PackageSpecificationInfo": "6.4.0",
                    "RunEnvironmentInfo": "5.3.0",
                    "subrule": "7.0.0",
                    "DefaultInfo": "0.0.1",
                    "__TestingOnly_NeverAvailable": "1000000000.0.0"
               },
               "legacy_globals": {
                    "JavaInfo": "8.0.0",
                    "JavaPluginInfo": "8.0.0",
                    "ProtoInfo": "8.0.0",
                    "PyCcLinkParamsProvider": "8.0.0",
                    "PyInfo": "8.0.0",
                    "PyRuntimeInfo": "8.0.0",
                    "cc_proto_aspect": "8.0.0"
               }
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_features+//private:globals_repo.bzl%globals_repo",
                    "attributes": {
                         "name": "bazel_features++version_extension+bazel_features_globals",
                         "globals": {
                              "CcSharedLibraryInfo": "6.0.0-pre.20220630.1",
                              "CcSharedLibraryHintInfo": "7.0.0-pre.20230316.2",
                              "macro": "8.0.0",
                              "PackageSpecificationInfo": "6.4.0",
                              "RunEnvironmentInfo": "5.3.0",
                              "subrule": "7.0.0",
                              "DefaultInfo": "0.0.1",
                              "__TestingOnly_NeverAvailable": "1000000000.0.0"
                         },
                         "legacy_globals": {
                              "JavaInfo": "8.0.0",
                              "JavaPluginInfo": "8.0.0",
                              "ProtoInfo": "8.0.0",
                              "PyCcLinkParamsProvider": "8.0.0",
                              "PyInfo": "8.0.0",
                              "PyRuntimeInfo": "8.0.0",
                              "cc_proto_aspect": "8.0.0"
                         }
                    },
                    "output_tree_hash": "6b2cc2db574126ef2b694118e829b9a0232e280edb6e1b0b24fbb3185f9cce40"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_features+//private:version_repo.bzl%version_repo",
          "definition_information": "Repository bazel_features++version_extension+bazel_features_version instantiated at:\n  <builtin>: in <toplevel>\nRepository rule version_repo defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/bazel_features+/private/version_repo.bzl:20:31: in <toplevel>\n",
          "original_attributes": {
               "name": "bazel_features++version_extension+bazel_features_version"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_features+//private:version_repo.bzl%version_repo",
                    "attributes": {
                         "name": "bazel_features++version_extension+bazel_features_version"
                    },
                    "output_tree_hash": "f7e037c76644a36a35437e8ffc61db400913736a561e3b8a70fd7e730bb10d30"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository googleapis-rules-registry+ instantiated at:\n  <builtin>: in <toplevel>\nRepository rule http_archive defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/bazel_tools/tools/build_defs/repo/http.bzl:431:31: in <toplevel>\n",
          "original_attributes": {
               "name": "googleapis-rules-registry+",
               "urls": [
                    "https://github.com/fmeum/googleapis-rules-registry/releases/download/v1.0.0/googleapis-rules-registry-v1.0.0.tar.gz"
               ],
               "integrity": "sha256-r3sJhxbaJDSFqR4eZ5ssfI7ii7ORtzTdyxrc5amS6b4=",
               "strip_prefix": "googleapis-rules-registry",
               "remote_file_urls": {},
               "remote_file_integrity": {},
               "remote_module_file_urls": [
                    "https://bcr.bazel.build/modules/googleapis-rules-registry/1.0.0/MODULE.bazel"
               ],
               "remote_module_file_integrity": "sha256-l8ak1BOzc9TMlwZdo94bIWbiLLu19MyfBXYL+oNhniQ=",
               "remote_patches": {},
               "remote_patch_strip": 0
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "name": "googleapis-rules-registry+",
                         "urls": [
                              "https://github.com/fmeum/googleapis-rules-registry/releases/download/v1.0.0/googleapis-rules-registry-v1.0.0.tar.gz"
                         ],
                         "integrity": "sha256-r3sJhxbaJDSFqR4eZ5ssfI7ii7ORtzTdyxrc5amS6b4=",
                         "strip_prefix": "googleapis-rules-registry",
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_module_file_urls": [
                              "https://bcr.bazel.build/modules/googleapis-rules-registry/1.0.0/MODULE.bazel"
                         ],
                         "remote_module_file_integrity": "sha256-l8ak1BOzc9TMlwZdo94bIWbiLLu19MyfBXYL+oNhniQ=",
                         "remote_patches": {},
                         "remote_patch_strip": 0
                    },
                    "output_tree_hash": "34713b2aca51de1a79480d16886c6638aebf98b7d430dedc089c2a2a6f7bb25a"
               }
          ]
     },
     {
          "original_rule_class": "@@googleapis-rules-registry+//private/extensions:rules_registry.bzl%_imports",
          "definition_information": "Repository googleapis-rules-registry++rules_registry+com_google_googleapis_imports instantiated at:\n  <builtin>: in <toplevel>\nRepository rule _imports defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/googleapis-rules-registry+/private/extensions/rules_registry.bzl:39:27: in <toplevel>\n",
          "original_attributes": {
               "name": "googleapis-rules-registry++rules_registry+com_google_googleapis_imports",
               "rules": {
                    "cc_gapic_library": "",
                    "cc_grpc_library": "@@grpc+//bazel:cc_grpc_library.bzl",
                    "cc_proto_library": "@@protobuf+//bazel:cc_proto_library.bzl",
                    "csharp_gapic_assembly_pkg": "",
                    "csharp_gapic_library": "",
                    "csharp_grpc_library": "",
                    "csharp_proto_library": "",
                    "go_gapic_assembly_pkg": "",
                    "go_gapic_library": "",
                    "go_grpc_library": "",
                    "go_library": "",
                    "go_proto_library": "",
                    "go_test": "",
                    "java_gapic_assembly_gradle_pkg": "",
                    "java_gapic_library": "",
                    "java_gapic_test": "",
                    "java_grpc_library": "",
                    "java_proto_library": "",
                    "moved_proto_library": "",
                    "nodejs_gapic_assembly_pkg": "",
                    "nodejs_gapic_library": "",
                    "php_gapic_assembly_pkg": "",
                    "php_gapic_library": "",
                    "php_grpc_library": "",
                    "php_proto_library": "",
                    "proto_library_with_info": "",
                    "py_gapic_assembly_pkg": "",
                    "py_gapic_library": "",
                    "py_grpc_library": "",
                    "py_import": "",
                    "py_proto_library": "",
                    "py_test": "",
                    "ruby_ads_gapic_library": "",
                    "ruby_cloud_gapic_library": "",
                    "ruby_gapic_assembly_pkg": "",
                    "ruby_grpc_library": "",
                    "ruby_proto_library": ""
               }
          },
          "repositories": [
               {
                    "rule_class": "@@googleapis-rules-registry+//private/extensions:rules_registry.bzl%_imports",
                    "attributes": {
                         "name": "googleapis-rules-registry++rules_registry+com_google_googleapis_imports",
                         "rules": {
                              "cc_gapic_library": "",
                              "cc_grpc_library": "@@grpc+//bazel:cc_grpc_library.bzl",
                              "cc_proto_library": "@@protobuf+//bazel:cc_proto_library.bzl",
                              "csharp_gapic_assembly_pkg": "",
                              "csharp_gapic_library": "",
                              "csharp_grpc_library": "",
                              "csharp_proto_library": "",
                              "go_gapic_assembly_pkg": "",
                              "go_gapic_library": "",
                              "go_grpc_library": "",
                              "go_library": "",
                              "go_proto_library": "",
                              "go_test": "",
                              "java_gapic_assembly_gradle_pkg": "",
                              "java_gapic_library": "",
                              "java_gapic_test": "",
                              "java_grpc_library": "",
                              "java_proto_library": "",
                              "moved_proto_library": "",
                              "nodejs_gapic_assembly_pkg": "",
                              "nodejs_gapic_library": "",
                              "php_gapic_assembly_pkg": "",
                              "php_gapic_library": "",
                              "php_grpc_library": "",
                              "php_proto_library": "",
                              "proto_library_with_info": "",
                              "py_gapic_assembly_pkg": "",
                              "py_gapic_library": "",
                              "py_grpc_library": "",
                              "py_import": "",
                              "py_proto_library": "",
                              "py_test": "",
                              "ruby_ads_gapic_library": "",
                              "ruby_cloud_gapic_library": "",
                              "ruby_gapic_assembly_pkg": "",
                              "ruby_grpc_library": "",
                              "ruby_proto_library": ""
                         }
                    },
                    "output_tree_hash": "6fc7bade367d254b2977e83bd8264ad292b30c048d9a0cc711d8eaebf1e26d43"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository rules_proto+ instantiated at:\n  <builtin>: in <toplevel>\nRepository rule http_archive defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/bazel_tools/tools/build_defs/repo/http.bzl:431:31: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_proto+",
               "urls": [
                    "https://github.com/bazelbuild/rules_proto/releases/download/7.1.0/rules_proto-7.1.0.tar.gz"
               ],
               "integrity": "sha256-FKIlhwq06RhpZSz9ae8gKCd/wdxJENZdNTti1uCuIfQ=",
               "strip_prefix": "rules_proto-7.1.0",
               "remote_file_urls": {},
               "remote_file_integrity": {},
               "remote_module_file_urls": [
                    "https://bcr.bazel.build/modules/rules_proto/7.1.0/MODULE.bazel"
               ],
               "remote_module_file_integrity": "sha256-AC1i2RCPdbuAfNViRdRWSPOCdcs6mdzUXfuGTF10y5Y=",
               "remote_patches": {
                    "https://bcr.bazel.build/modules/rules_proto/7.1.0/patches/module_dot_bazel_version.patch": "sha256-GFtfNnjXlShEmp3o0HiTq8AWf0YpNxLkmGVMt98QcfI=",
                    "https://bcr.bazel.build/modules/rules_proto/7.1.0/patches/MODULE.bazel.patch": "sha256-QC5hjx/QZTZ3deil1x9qT0Ni6G1+ZiFaQ+xGHtXR0HE="
               },
               "remote_patch_strip": 1
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "name": "rules_proto+",
                         "urls": [
                              "https://github.com/bazelbuild/rules_proto/releases/download/7.1.0/rules_proto-7.1.0.tar.gz"
                         ],
                         "integrity": "sha256-FKIlhwq06RhpZSz9ae8gKCd/wdxJENZdNTti1uCuIfQ=",
                         "strip_prefix": "rules_proto-7.1.0",
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_module_file_urls": [
                              "https://bcr.bazel.build/modules/rules_proto/7.1.0/MODULE.bazel"
                         ],
                         "remote_module_file_integrity": "sha256-AC1i2RCPdbuAfNViRdRWSPOCdcs6mdzUXfuGTF10y5Y=",
                         "remote_patches": {
                              "https://bcr.bazel.build/modules/rules_proto/7.1.0/patches/module_dot_bazel_version.patch": "sha256-GFtfNnjXlShEmp3o0HiTq8AWf0YpNxLkmGVMt98QcfI=",
                              "https://bcr.bazel.build/modules/rules_proto/7.1.0/patches/MODULE.bazel.patch": "sha256-QC5hjx/QZTZ3deil1x9qT0Ni6G1+ZiFaQ+xGHtXR0HE="
                         },
                         "remote_patch_strip": 1
                    },
                    "output_tree_hash": "72a448cb77793835db3872e77426d5fc424db02fd8f09c5474d2904f7653f350"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository grpc+ instantiated at:\n  <builtin>: in <toplevel>\nRepository rule http_archive defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/bazel_tools/tools/build_defs/repo/http.bzl:431:31: in <toplevel>\n",
          "original_attributes": {
               "name": "grpc+",
               "urls": [
                    "https://github.com/grpc/grpc/archive/refs/tags/v1.72.0.tar.gz"
               ],
               "integrity": "sha256-SoqpnV4k+A6mt+yVRj4Wr1vZGqgF4mxmHvZJGuPS0jw=",
               "strip_prefix": "grpc-1.72.0",
               "remote_file_urls": {},
               "remote_file_integrity": {},
               "remote_module_file_urls": [
                    "https://bcr.bazel.build/modules/grpc/1.72.0/MODULE.bazel"
               ],
               "remote_module_file_integrity": "sha256-sqguJnhxdoP5GKyHNkAF/Qvzrjv8qbDK5o6Ri6QllLE=",
               "remote_patches": {
                    "https://bcr.bazel.build/modules/grpc/1.72.0/patches/adopt_bzlmod.patch": "sha256-d7z79/WSEiNTZiQ/A50HMbyqbZj3qIESa4H2n/yhlhA="
               },
               "remote_patch_strip": 1
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "name": "grpc+",
                         "urls": [
                              "https://github.com/grpc/grpc/archive/refs/tags/v1.72.0.tar.gz"
                         ],
                         "integrity": "sha256-SoqpnV4k+A6mt+yVRj4Wr1vZGqgF4mxmHvZJGuPS0jw=",
                         "strip_prefix": "grpc-1.72.0",
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_module_file_urls": [
                              "https://bcr.bazel.build/modules/grpc/1.72.0/MODULE.bazel"
                         ],
                         "remote_module_file_integrity": "sha256-sqguJnhxdoP5GKyHNkAF/Qvzrjv8qbDK5o6Ri6QllLE=",
                         "remote_patches": {
                              "https://bcr.bazel.build/modules/grpc/1.72.0/patches/adopt_bzlmod.patch": "sha256-d7z79/WSEiNTZiQ/A50HMbyqbZj3qIESa4H2n/yhlhA="
                         },
                         "remote_patch_strip": 1
                    },
                    "output_tree_hash": "dcd7e8e387f2f2a45ee324cd58940feddf840b5be6f2e98c8913131d5fe1953a"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository platforms instantiated at:\n  <builtin>: in <toplevel>\nRepository rule http_archive defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/bazel_tools/tools/build_defs/repo/http.bzl:431:31: in <toplevel>\n",
          "original_attributes": {
               "name": "platforms",
               "urls": [
                    "https://github.com/bazelbuild/platforms/releases/download/0.0.11/platforms-0.0.11.tar.gz"
               ],
               "integrity": "sha256-KXQuhydYCbXlmNwvBNhpYMx6VbMGfZciHJq7yZJr/w8=",
               "strip_prefix": "",
               "remote_file_urls": {},
               "remote_file_integrity": {},
               "remote_module_file_urls": [
                    "https://bcr.bazel.build/modules/platforms/0.0.11/MODULE.bazel"
               ],
               "remote_module_file_integrity": "sha256-Da78SXMuInyqi/qDTWXcUujMGKL6+A3yXoyuoVGpQT8=",
               "remote_patches": {},
               "remote_patch_strip": 0
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "name": "platforms",
                         "urls": [
                              "https://github.com/bazelbuild/platforms/releases/download/0.0.11/platforms-0.0.11.tar.gz"
                         ],
                         "integrity": "sha256-KXQuhydYCbXlmNwvBNhpYMx6VbMGfZciHJq7yZJr/w8=",
                         "strip_prefix": "",
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_module_file_urls": [
                              "https://bcr.bazel.build/modules/platforms/0.0.11/MODULE.bazel"
                         ],
                         "remote_module_file_integrity": "sha256-Da78SXMuInyqi/qDTWXcUujMGKL6+A3yXoyuoVGpQT8=",
                         "remote_patches": {},
                         "remote_patch_strip": 0
                    },
                    "output_tree_hash": "99a6cd4e8e1cea4d92d00adc57565167be1b35b303dab3d1835a912d87137e67"
               }
          ]
     },
     {
          "original_rule_class": "@@platforms//host:extension.bzl%host_platform_repo",
          "definition_information": "Repository platforms+host_platform+host_platform instantiated at:\n  <builtin>: in <toplevel>\nRepository rule host_platform_repo defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/platforms/host/extension.bzl:53:37: in <toplevel>\n",
          "original_attributes": {
               "name": "platforms+host_platform+host_platform"
          },
          "repositories": [
               {
                    "rule_class": "@@platforms//host:extension.bzl%host_platform_repo",
                    "attributes": {
                         "name": "platforms+host_platform+host_platform"
                    },
                    "output_tree_hash": "2512c4cff0afebd4bf7e21beeb2331c4b2aa3849da1b1cbf7259b368b7f79cba"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository rules_license+ instantiated at:\n  <builtin>: in <toplevel>\nRepository rule http_archive defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/bazel_tools/tools/build_defs/repo/http.bzl:431:31: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_license+",
               "urls": [
                    "https://github.com/bazelbuild/rules_license/releases/download/1.0.0/rules_license-1.0.0.tar.gz"
               ],
               "integrity": "sha256-JtQCH2iY4juC75UweDid1JrCtWGKxWSt5O+HzO0Uezg=",
               "strip_prefix": "",
               "remote_file_urls": {},
               "remote_file_integrity": {},
               "remote_module_file_urls": [
                    "https://bcr.bazel.build/modules/rules_license/1.0.0/MODULE.bazel"
               ],
               "remote_module_file_integrity": "sha256-p/2mDu/fPYyCcmK6SZlX5N8G9lkzC75s29uXW3aLtlw=",
               "remote_patches": {},
               "remote_patch_strip": 0
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "name": "rules_license+",
                         "urls": [
                              "https://github.com/bazelbuild/rules_license/releases/download/1.0.0/rules_license-1.0.0.tar.gz"
                         ],
                         "integrity": "sha256-JtQCH2iY4juC75UweDid1JrCtWGKxWSt5O+HzO0Uezg=",
                         "strip_prefix": "",
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_module_file_urls": [
                              "https://bcr.bazel.build/modules/rules_license/1.0.0/MODULE.bazel"
                         ],
                         "remote_module_file_integrity": "sha256-p/2mDu/fPYyCcmK6SZlX5N8G9lkzC75s29uXW3aLtlw=",
                         "remote_patches": {},
                         "remote_patch_strip": 0
                    },
                    "output_tree_hash": "52fcb75250774d2a3f23d4d894043ae68775ae11a588d42ff5542b7b8cd616f8"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository rules_pkg+ instantiated at:\n  <builtin>: in <toplevel>\nRepository rule http_archive defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/bazel_tools/tools/build_defs/repo/http.bzl:431:31: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_pkg+",
               "urls": [
                    "https://github.com/bazelbuild/rules_pkg/releases/download/1.0.1/rules_pkg-1.0.1.tar.gz"
               ],
               "integrity": "sha256-0gyVGWDtd8t7NBwqWUiFNOSU1a0dMMSBjHNtV3cqn+8=",
               "strip_prefix": "",
               "remote_file_urls": {},
               "remote_file_integrity": {},
               "remote_module_file_urls": [
                    "https://bcr.bazel.build/modules/rules_pkg/1.0.1/MODULE.bazel"
               ],
               "remote_module_file_integrity": "sha256-Wx35fbwpYjvM3ysNzQ9csI4vLJBQqrEJL9OaQegmhv8=",
               "remote_patches": {},
               "remote_patch_strip": 0
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "name": "rules_pkg+",
                         "urls": [
                              "https://github.com/bazelbuild/rules_pkg/releases/download/1.0.1/rules_pkg-1.0.1.tar.gz"
                         ],
                         "integrity": "sha256-0gyVGWDtd8t7NBwqWUiFNOSU1a0dMMSBjHNtV3cqn+8=",
                         "strip_prefix": "",
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_module_file_urls": [
                              "https://bcr.bazel.build/modules/rules_pkg/1.0.1/MODULE.bazel"
                         ],
                         "remote_module_file_integrity": "sha256-Wx35fbwpYjvM3ysNzQ9csI4vLJBQqrEJL9OaQegmhv8=",
                         "remote_patches": {},
                         "remote_patch_strip": 0
                    },
                    "output_tree_hash": "eff72c8c82cb03d3341ef18a8a47141a7aa30da2814c4556af565cd9cd6e5327"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_cc+//cc/private/toolchain:cc_configure.bzl%cc_autoconf_toolchains",
          "definition_information": "Repository rules_cc++cc_configure_extension+local_config_cc_toolchains instantiated at:\n  <builtin>: in <toplevel>\nRepository rule cc_autoconf_toolchains defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/rules_cc+/cc/private/toolchain/cc_configure.bzl:47:41: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_cc++cc_configure_extension+local_config_cc_toolchains"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_cc+//cc/private/toolchain:cc_configure.bzl%cc_autoconf_toolchains",
                    "attributes": {
                         "name": "rules_cc++cc_configure_extension+local_config_cc_toolchains"
                    },
                    "output_tree_hash": "7b227a4801ff89c05f4b7925782a0379b253250735d4c6d218c3de09884898c1"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_python+//python/uv/private:uv_toolchains_repo.bzl%uv_toolchains_repo",
          "definition_information": "Repository rules_python++uv+uv instantiated at:\n  <builtin>: in <toplevel>\nRepository rule uv_toolchains_repo defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/rules_python+/python/uv/private/uv_toolchains_repo.bzl:49:37: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_python++uv+uv",
               "toolchain_compatible_with": {
                    "none": [
                         "@platforms//:incompatible"
                    ]
               },
               "toolchain_implementations": {
                    "none": "@@rules_python+//python:none"
               },
               "toolchain_names": [
                    "none"
               ],
               "toolchain_target_settings": {},
               "toolchain_type": "@@rules_python+//python/uv:uv_toolchain_type"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_python+//python/uv/private:uv_toolchains_repo.bzl%uv_toolchains_repo",
                    "attributes": {
                         "name": "rules_python++uv+uv",
                         "toolchain_compatible_with": {
                              "none": [
                                   "@platforms//:incompatible"
                              ]
                         },
                         "toolchain_implementations": {
                              "none": "@@rules_python+//python:none"
                         },
                         "toolchain_names": [
                              "none"
                         ],
                         "toolchain_target_settings": {},
                         "toolchain_type": "@@rules_python+//python/uv:uv_toolchain_type"
                    },
                    "output_tree_hash": "8e7b44a2fb3f61bb1a49835b86f7a4b50d463823c7954a453989953c1041fa41"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_python+//python/private:pythons_hub.bzl%hub_repo",
          "definition_information": "Repository rules_python++python+pythons_hub instantiated at:\n  <builtin>: in <toplevel>\nRepository rule hub_repo defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/rules_python+/python/private/pythons_hub.bzl:145:27: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_python++python+pythons_hub",
               "default_python_version": "3.11",
               "loaded_platforms": {
                    "3.9.21": [
                         "aarch64-apple-darwin",
                         "aarch64-unknown-linux-gnu",
                         "ppc64le-unknown-linux-gnu",
                         "riscv64-unknown-linux-gnu",
                         "s390x-unknown-linux-gnu",
                         "x86_64-apple-darwin",
                         "x86_64-pc-windows-msvc",
                         "x86_64-unknown-linux-gnu",
                         "x86_64-unknown-linux-musl"
                    ],
                    "3.10.16": [
                         "aarch64-apple-darwin",
                         "aarch64-unknown-linux-gnu",
                         "ppc64le-unknown-linux-gnu",
                         "riscv64-unknown-linux-gnu",
                         "s390x-unknown-linux-gnu",
                         "x86_64-apple-darwin",
                         "x86_64-pc-windows-msvc",
                         "x86_64-unknown-linux-gnu",
                         "x86_64-unknown-linux-musl"
                    ],
                    "3.12.9": [
                         "aarch64-apple-darwin",
                         "aarch64-unknown-linux-gnu",
                         "ppc64le-unknown-linux-gnu",
                         "riscv64-unknown-linux-gnu",
                         "s390x-unknown-linux-gnu",
                         "x86_64-apple-darwin",
                         "x86_64-pc-windows-msvc",
                         "x86_64-unknown-linux-gnu",
                         "x86_64-unknown-linux-musl"
                    ],
                    "3.8.20": [
                         "aarch64-apple-darwin",
                         "aarch64-unknown-linux-gnu",
                         "x86_64-apple-darwin",
                         "x86_64-pc-windows-msvc",
                         "x86_64-unknown-linux-gnu"
                    ],
                    "3.13.2": [
                         "aarch64-apple-darwin",
                         "aarch64-apple-darwin-freethreaded",
                         "aarch64-unknown-linux-gnu",
                         "aarch64-unknown-linux-gnu-freethreaded",
                         "ppc64le-unknown-linux-gnu",
                         "ppc64le-unknown-linux-gnu-freethreaded",
                         "riscv64-unknown-linux-gnu",
                         "riscv64-unknown-linux-gnu-freethreaded",
                         "s390x-unknown-linux-gnu",
                         "s390x-unknown-linux-gnu-freethreaded",
                         "x86_64-apple-darwin",
                         "x86_64-apple-darwin-freethreaded",
                         "x86_64-pc-windows-msvc",
                         "x86_64-pc-windows-msvc-freethreaded",
                         "x86_64-unknown-linux-gnu",
                         "x86_64-unknown-linux-gnu-freethreaded",
                         "x86_64-unknown-linux-musl"
                    ],
                    "3.11.11": [
                         "aarch64-apple-darwin",
                         "aarch64-unknown-linux-gnu",
                         "ppc64le-unknown-linux-gnu",
                         "riscv64-unknown-linux-gnu",
                         "s390x-unknown-linux-gnu",
                         "x86_64-apple-darwin",
                         "x86_64-pc-windows-msvc",
                         "x86_64-unknown-linux-gnu",
                         "x86_64-unknown-linux-musl"
                    ]
               },
               "minor_mapping": {
                    "3.8": "3.8.20",
                    "3.9": "3.9.21",
                    "3.10": "3.10.16",
                    "3.11": "3.11.11",
                    "3.12": "3.12.9",
                    "3.13": "3.13.2"
               },
               "python_versions": [
                    "3.8.20",
                    "3.9.10",
                    "3.9.12",
                    "3.9.13",
                    "3.9.15",
                    "3.9.16",
                    "3.9.17",
                    "3.9.18",
                    "3.9.19",
                    "3.9.20",
                    "3.9.21",
                    "3.10.2",
                    "3.10.4",
                    "3.10.6",
                    "3.10.8",
                    "3.10.9",
                    "3.10.11",
                    "3.10.12",
                    "3.10.13",
                    "3.10.14",
                    "3.10.15",
                    "3.10.16",
                    "3.11.1",
                    "3.11.3",
                    "3.11.4",
                    "3.11.5",
                    "3.11.6",
                    "3.11.7",
                    "3.11.8",
                    "3.11.9",
                    "3.11.10",
                    "3.11.11",
                    "3.12.0",
                    "3.12.1",
                    "3.12.2",
                    "3.12.3",
                    "3.12.4",
                    "3.12.7",
                    "3.12.8",
                    "3.12.9",
                    "3.13.0",
                    "3.13.1",
                    "3.13.2"
               ],
               "toolchain_prefixes": [
                    "_0000_python_3_9_",
                    "_0001_python_3_10_",
                    "_0002_python_3_12_",
                    "_0003_python_3_8_",
                    "_0004_python_3_13_",
                    "_0005_python_3_11_"
               ],
               "toolchain_python_versions": [
                    "3.9.21",
                    "3.10.16",
                    "3.12.9",
                    "3.8.20",
                    "3.13.2",
                    "3.11.11"
               ],
               "toolchain_set_python_version_constraints": [
                    "True",
                    "True",
                    "True",
                    "True",
                    "True",
                    "False"
               ],
               "toolchain_user_repository_names": [
                    "python_3_9",
                    "python_3_10",
                    "python_3_12",
                    "python_3_8",
                    "python_3_13",
                    "python_3_11"
               ]
          },
          "repositories": [
               {
                    "rule_class": "@@rules_python+//python/private:pythons_hub.bzl%hub_repo",
                    "attributes": {
                         "name": "rules_python++python+pythons_hub",
                         "default_python_version": "3.11",
                         "loaded_platforms": {
                              "3.9.21": [
                                   "aarch64-apple-darwin",
                                   "aarch64-unknown-linux-gnu",
                                   "ppc64le-unknown-linux-gnu",
                                   "riscv64-unknown-linux-gnu",
                                   "s390x-unknown-linux-gnu",
                                   "x86_64-apple-darwin",
                                   "x86_64-pc-windows-msvc",
                                   "x86_64-unknown-linux-gnu",
                                   "x86_64-unknown-linux-musl"
                              ],
                              "3.10.16": [
                                   "aarch64-apple-darwin",
                                   "aarch64-unknown-linux-gnu",
                                   "ppc64le-unknown-linux-gnu",
                                   "riscv64-unknown-linux-gnu",
                                   "s390x-unknown-linux-gnu",
                                   "x86_64-apple-darwin",
                                   "x86_64-pc-windows-msvc",
                                   "x86_64-unknown-linux-gnu",
                                   "x86_64-unknown-linux-musl"
                              ],
                              "3.12.9": [
                                   "aarch64-apple-darwin",
                                   "aarch64-unknown-linux-gnu",
                                   "ppc64le-unknown-linux-gnu",
                                   "riscv64-unknown-linux-gnu",
                                   "s390x-unknown-linux-gnu",
                                   "x86_64-apple-darwin",
                                   "x86_64-pc-windows-msvc",
                                   "x86_64-unknown-linux-gnu",
                                   "x86_64-unknown-linux-musl"
                              ],
                              "3.8.20": [
                                   "aarch64-apple-darwin",
                                   "aarch64-unknown-linux-gnu",
                                   "x86_64-apple-darwin",
                                   "x86_64-pc-windows-msvc",
                                   "x86_64-unknown-linux-gnu"
                              ],
                              "3.13.2": [
                                   "aarch64-apple-darwin",
                                   "aarch64-apple-darwin-freethreaded",
                                   "aarch64-unknown-linux-gnu",
                                   "aarch64-unknown-linux-gnu-freethreaded",
                                   "ppc64le-unknown-linux-gnu",
                                   "ppc64le-unknown-linux-gnu-freethreaded",
                                   "riscv64-unknown-linux-gnu",
                                   "riscv64-unknown-linux-gnu-freethreaded",
                                   "s390x-unknown-linux-gnu",
                                   "s390x-unknown-linux-gnu-freethreaded",
                                   "x86_64-apple-darwin",
                                   "x86_64-apple-darwin-freethreaded",
                                   "x86_64-pc-windows-msvc",
                                   "x86_64-pc-windows-msvc-freethreaded",
                                   "x86_64-unknown-linux-gnu",
                                   "x86_64-unknown-linux-gnu-freethreaded",
                                   "x86_64-unknown-linux-musl"
                              ],
                              "3.11.11": [
                                   "aarch64-apple-darwin",
                                   "aarch64-unknown-linux-gnu",
                                   "ppc64le-unknown-linux-gnu",
                                   "riscv64-unknown-linux-gnu",
                                   "s390x-unknown-linux-gnu",
                                   "x86_64-apple-darwin",
                                   "x86_64-pc-windows-msvc",
                                   "x86_64-unknown-linux-gnu",
                                   "x86_64-unknown-linux-musl"
                              ]
                         },
                         "minor_mapping": {
                              "3.8": "3.8.20",
                              "3.9": "3.9.21",
                              "3.10": "3.10.16",
                              "3.11": "3.11.11",
                              "3.12": "3.12.9",
                              "3.13": "3.13.2"
                         },
                         "python_versions": [
                              "3.8.20",
                              "3.9.10",
                              "3.9.12",
                              "3.9.13",
                              "3.9.15",
                              "3.9.16",
                              "3.9.17",
                              "3.9.18",
                              "3.9.19",
                              "3.9.20",
                              "3.9.21",
                              "3.10.2",
                              "3.10.4",
                              "3.10.6",
                              "3.10.8",
                              "3.10.9",
                              "3.10.11",
                              "3.10.12",
                              "3.10.13",
                              "3.10.14",
                              "3.10.15",
                              "3.10.16",
                              "3.11.1",
                              "3.11.3",
                              "3.11.4",
                              "3.11.5",
                              "3.11.6",
                              "3.11.7",
                              "3.11.8",
                              "3.11.9",
                              "3.11.10",
                              "3.11.11",
                              "3.12.0",
                              "3.12.1",
                              "3.12.2",
                              "3.12.3",
                              "3.12.4",
                              "3.12.7",
                              "3.12.8",
                              "3.12.9",
                              "3.13.0",
                              "3.13.1",
                              "3.13.2"
                         ],
                         "toolchain_prefixes": [
                              "_0000_python_3_9_",
                              "_0001_python_3_10_",
                              "_0002_python_3_12_",
                              "_0003_python_3_8_",
                              "_0004_python_3_13_",
                              "_0005_python_3_11_"
                         ],
                         "toolchain_python_versions": [
                              "3.9.21",
                              "3.10.16",
                              "3.12.9",
                              "3.8.20",
                              "3.13.2",
                              "3.11.11"
                         ],
                         "toolchain_set_python_version_constraints": [
                              "True",
                              "True",
                              "True",
                              "True",
                              "True",
                              "False"
                         ],
                         "toolchain_user_repository_names": [
                              "python_3_9",
                              "python_3_10",
                              "python_3_12",
                              "python_3_8",
                              "python_3_13",
                              "python_3_11"
                         ]
                    },
                    "output_tree_hash": "d15cdf26189b095c65a8a9d7d1eac62b8f58b71e90eac7d41a0977f2cbe86dfe"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_shell+//shell/private/repositories:sh_config.bzl%sh_config",
          "definition_information": "Repository rules_shell++sh_configure+local_config_shell instantiated at:\n  <builtin>: in <toplevel>\nRepository rule sh_config defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/rules_shell+/shell/private/repositories/sh_config.bzl:88:28: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_shell++sh_configure+local_config_shell"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_shell+//shell/private/repositories:sh_config.bzl%sh_config",
                    "attributes": {
                         "name": "rules_shell++sh_configure+local_config_shell"
                    },
                    "output_tree_hash": "64371bf12e5127e46dca5ccad118b456fe46307e340ac58b232bb219075caeb0"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java+//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository rules_java++toolchains+remotejdk21_win_arm64_toolchain_config_repo instantiated at:\n  <builtin>: in <toplevel>\nRepository rule _toolchain_config defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/rules_java+/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_java++toolchains+remotejdk21_win_arm64_toolchain_config_repo",
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_21\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"21\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_win_arm64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_win_arm64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java+//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "rules_java++toolchains+remotejdk21_win_arm64_toolchain_config_repo",
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_21\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"21\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_win_arm64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_win_arm64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "db0b9619ae5f2884597cfc98a01c2b80cad33325e843d3484a8e11710b73a114"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java+//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository rules_java++toolchains+remotejdk21_win_toolchain_config_repo instantiated at:\n  <builtin>: in <toplevel>\nRepository rule _toolchain_config defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/rules_java+/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_java++toolchains+remotejdk21_win_toolchain_config_repo",
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_21\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"21\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_win//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_win//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java+//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "rules_java++toolchains+remotejdk21_win_toolchain_config_repo",
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_21\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"21\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_win//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_win//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "28f5a8bdc4d2d2afba0b9e5f68780a920fda69a95bf3be960ce923909cecfc78"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java+//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository rules_java++toolchains+remotejdk21_macos_aarch64_toolchain_config_repo instantiated at:\n  <builtin>: in <toplevel>\nRepository rule _toolchain_config defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/rules_java+/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_java++toolchains+remotejdk21_macos_aarch64_toolchain_config_repo",
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_21\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"21\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_macos_aarch64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_macos_aarch64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java+//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "rules_java++toolchains+remotejdk21_macos_aarch64_toolchain_config_repo",
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_21\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"21\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_macos_aarch64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_macos_aarch64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "d8865b83bedb371ccc273e9f748c76afbabd1ac306e02526b2ea99c1db37d922"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java+//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository rules_java++toolchains+remotejdk21_macos_toolchain_config_repo instantiated at:\n  <builtin>: in <toplevel>\nRepository rule _toolchain_config defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/rules_java+/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_java++toolchains+remotejdk21_macos_toolchain_config_repo",
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_21\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"21\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_macos//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_macos//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java+//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "rules_java++toolchains+remotejdk21_macos_toolchain_config_repo",
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_21\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"21\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_macos//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_macos//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "a057c60537bcda617ff67c8a5e51fd2152bddbffa3699f8489e1fba9891dbf4d"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java+//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository rules_java++toolchains+remotejdk21_linux_s390x_toolchain_config_repo instantiated at:\n  <builtin>: in <toplevel>\nRepository rule _toolchain_config defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/rules_java+/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_java++toolchains+remotejdk21_linux_s390x_toolchain_config_repo",
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_21\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"21\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux_s390x//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux_s390x//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java+//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "rules_java++toolchains+remotejdk21_linux_s390x_toolchain_config_repo",
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_21\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"21\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux_s390x//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux_s390x//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "75c96c0ec337cdbc1b45acbda38f7643d1403581d667dd9f24e5bc180c478844"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java+//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository rules_java++toolchains+remotejdk21_linux_riscv64_toolchain_config_repo instantiated at:\n  <builtin>: in <toplevel>\nRepository rule _toolchain_config defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/rules_java+/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_java++toolchains+remotejdk21_linux_riscv64_toolchain_config_repo",
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_21\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"21\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:riscv64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux_riscv64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:riscv64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux_riscv64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java+//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "rules_java++toolchains+remotejdk21_linux_riscv64_toolchain_config_repo",
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_21\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"21\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:riscv64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux_riscv64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:riscv64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux_riscv64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "3b9a11dfa44b19750eb99850e52e64de5d89520a3047831fefca0b56c5231e90"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java+//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository rules_java++toolchains+remotejdk21_linux_ppc64le_toolchain_config_repo instantiated at:\n  <builtin>: in <toplevel>\nRepository rule _toolchain_config defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/rules_java+/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_java++toolchains+remotejdk21_linux_ppc64le_toolchain_config_repo",
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_21\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"21\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:ppc64le\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux_ppc64le//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:ppc64le\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux_ppc64le//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java+//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "rules_java++toolchains+remotejdk21_linux_ppc64le_toolchain_config_repo",
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_21\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"21\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:ppc64le\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux_ppc64le//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:ppc64le\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux_ppc64le//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "7c6515785867543e8490aa27a11b4f90a9a84ccda924afdb5a89339764bd2dc2"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java+//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository rules_java++toolchains+remotejdk21_linux_aarch64_toolchain_config_repo instantiated at:\n  <builtin>: in <toplevel>\nRepository rule _toolchain_config defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/rules_java+/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_java++toolchains+remotejdk21_linux_aarch64_toolchain_config_repo",
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_21\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"21\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux_aarch64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux_aarch64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java+//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "rules_java++toolchains+remotejdk21_linux_aarch64_toolchain_config_repo",
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_21\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"21\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux_aarch64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux_aarch64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "005e24817286b54267ad7ea8e475610f01df05403646bba4922d808c86ba1809"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java+//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository rules_java++toolchains+remotejdk21_linux_toolchain_config_repo instantiated at:\n  <builtin>: in <toplevel>\nRepository rule _toolchain_config defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/rules_java+/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_java++toolchains+remotejdk21_linux_toolchain_config_repo",
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_21\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"21\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java+//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "rules_java++toolchains+remotejdk21_linux_toolchain_config_repo",
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_21\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"21\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "458b23f83f60965d800755226ede286805cc61acd618389e9237764f6b08ef6b"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java+//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository rules_java++toolchains+remotejdk17_win_arm64_toolchain_config_repo instantiated at:\n  <builtin>: in <toplevel>\nRepository rule _toolchain_config defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/rules_java+/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_java++toolchains+remotejdk17_win_arm64_toolchain_config_repo",
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_win_arm64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_win_arm64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java+//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "rules_java++toolchains+remotejdk17_win_arm64_toolchain_config_repo",
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_win_arm64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_win_arm64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "dd9d26712ec6aac2231d7d27320d7c9ae0d1d6c04df09241a1791e00aba09024"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java+//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository rules_java++toolchains+remotejdk17_win_toolchain_config_repo instantiated at:\n  <builtin>: in <toplevel>\nRepository rule _toolchain_config defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/rules_java+/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_java++toolchains+remotejdk17_win_toolchain_config_repo",
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_win//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_win//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java+//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "rules_java++toolchains+remotejdk17_win_toolchain_config_repo",
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_win//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_win//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "3dd77804474ffcaaadbb9c40faa35f16ff8b3252c4b1f54d3814c7a3b01998a0"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java+//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository rules_java++toolchains+remotejdk17_macos_aarch64_toolchain_config_repo instantiated at:\n  <builtin>: in <toplevel>\nRepository rule _toolchain_config defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/rules_java+/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_java++toolchains+remotejdk17_macos_aarch64_toolchain_config_repo",
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_macos_aarch64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_macos_aarch64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java+//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "rules_java++toolchains+remotejdk17_macos_aarch64_toolchain_config_repo",
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_macos_aarch64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_macos_aarch64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "9cbee14f44320f0069bee2c0ce447c4895b587962ec3f4c60c79ff78f6971319"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java+//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository rules_java++toolchains+remotejdk17_macos_toolchain_config_repo instantiated at:\n  <builtin>: in <toplevel>\nRepository rule _toolchain_config defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/rules_java+/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_java++toolchains+remotejdk17_macos_toolchain_config_repo",
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_macos//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_macos//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java+//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "rules_java++toolchains+remotejdk17_macos_toolchain_config_repo",
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_macos//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_macos//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "bd155dde49005240e8bccb59471e8e180ebee84302cc44e4d94c04d8a23cc868"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java+//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository rules_java++toolchains+remotejdk17_linux_s390x_toolchain_config_repo instantiated at:\n  <builtin>: in <toplevel>\nRepository rule _toolchain_config defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/rules_java+/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_java++toolchains+remotejdk17_linux_s390x_toolchain_config_repo",
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux_s390x//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux_s390x//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java+//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "rules_java++toolchains+remotejdk17_linux_s390x_toolchain_config_repo",
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux_s390x//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux_s390x//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "4f6fa1ce29d5c18904ef260290de78049dca844a5c2ed54ab5a662fd4bffc671"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java+//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository rules_java++toolchains+remotejdk17_linux_ppc64le_toolchain_config_repo instantiated at:\n  <builtin>: in <toplevel>\nRepository rule _toolchain_config defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/rules_java+/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_java++toolchains+remotejdk17_linux_ppc64le_toolchain_config_repo",
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:ppc64le\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux_ppc64le//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:ppc64le\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux_ppc64le//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java+//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "rules_java++toolchains+remotejdk17_linux_ppc64le_toolchain_config_repo",
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:ppc64le\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux_ppc64le//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:ppc64le\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux_ppc64le//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "23e689b235907bbc041118c33f418258b77f5f8d24c8828c0ba69b6c12555fba"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java+//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository rules_java++toolchains+remotejdk17_linux_aarch64_toolchain_config_repo instantiated at:\n  <builtin>: in <toplevel>\nRepository rule _toolchain_config defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/rules_java+/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_java++toolchains+remotejdk17_linux_aarch64_toolchain_config_repo",
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux_aarch64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux_aarch64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java+//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "rules_java++toolchains+remotejdk17_linux_aarch64_toolchain_config_repo",
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux_aarch64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux_aarch64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "08e1cf36ae45153692368b757dabe08c0dbeb0c8a26297bd5ad6a041e54eed50"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java+//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository rules_java++toolchains+remotejdk17_linux_toolchain_config_repo instantiated at:\n  <builtin>: in <toplevel>\nRepository rule _toolchain_config defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/rules_java+/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_java++toolchains+remotejdk17_linux_toolchain_config_repo",
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java+//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "rules_java++toolchains+remotejdk17_linux_toolchain_config_repo",
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "cf31184cb68d8d6417d6a41d20524af854e5242306e2e89b778020888b2d9edd"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java+//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository rules_java++toolchains+remotejdk11_win_arm64_toolchain_config_repo instantiated at:\n  <builtin>: in <toplevel>\nRepository rule _toolchain_config defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/rules_java+/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_java++toolchains+remotejdk11_win_arm64_toolchain_config_repo",
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_win_arm64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_win_arm64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java+//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "rules_java++toolchains+remotejdk11_win_arm64_toolchain_config_repo",
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_win_arm64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_win_arm64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "849b17f1cad87b084b1eab38ef5d774c9d8c38f184e01ad2c228338663ef0ae1"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java+//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository rules_java++toolchains+remotejdk11_win_toolchain_config_repo instantiated at:\n  <builtin>: in <toplevel>\nRepository rule _toolchain_config defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/rules_java+/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_java++toolchains+remotejdk11_win_toolchain_config_repo",
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_win//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_win//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java+//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "rules_java++toolchains+remotejdk11_win_toolchain_config_repo",
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_win//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_win//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "8788fab9db7b0ca796c057f7c344aed59c539ced21b5f868b18e809f6c6536f5"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java+//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository rules_java++toolchains+remotejdk11_macos_aarch64_toolchain_config_repo instantiated at:\n  <builtin>: in <toplevel>\nRepository rule _toolchain_config defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/rules_java+/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_java++toolchains+remotejdk11_macos_aarch64_toolchain_config_repo",
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_macos_aarch64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_macos_aarch64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java+//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "rules_java++toolchains+remotejdk11_macos_aarch64_toolchain_config_repo",
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_macos_aarch64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_macos_aarch64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "b9faea632b93fcddbce9e8f7f6751a061d5ae01a780a7c7c0097a0db2cc7b378"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java+//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository rules_java++toolchains+remotejdk11_macos_toolchain_config_repo instantiated at:\n  <builtin>: in <toplevel>\nRepository rule _toolchain_config defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/rules_java+/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_java++toolchains+remotejdk11_macos_toolchain_config_repo",
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_macos//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_macos//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java+//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "rules_java++toolchains+remotejdk11_macos_toolchain_config_repo",
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_macos//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_macos//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "c18218123acb7bd028cfdec5456392801ae61cf6072b32b5cf97adf87c57825b"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java+//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository rules_java++toolchains+remotejdk11_linux_s390x_toolchain_config_repo instantiated at:\n  <builtin>: in <toplevel>\nRepository rule _toolchain_config defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/rules_java+/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_java++toolchains+remotejdk11_linux_s390x_toolchain_config_repo",
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_s390x//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_s390x//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java+//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "rules_java++toolchains+remotejdk11_linux_s390x_toolchain_config_repo",
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_s390x//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_s390x//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "4f363c8c2e8539dbb03f2a0b800b7769c4170b1d9ec9a97f685ec7c302311467"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java+//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository rules_java++toolchains+remotejdk11_linux_ppc64le_toolchain_config_repo instantiated at:\n  <builtin>: in <toplevel>\nRepository rule _toolchain_config defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/rules_java+/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_java++toolchains+remotejdk11_linux_ppc64le_toolchain_config_repo",
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:ppc64le\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_ppc64le//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:ppc64le\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_ppc64le//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java+//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "rules_java++toolchains+remotejdk11_linux_ppc64le_toolchain_config_repo",
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:ppc64le\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_ppc64le//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:ppc64le\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_ppc64le//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "e448b19f2a59a97492cdaa101ace2db6274a952cbe65f0a9494d7a34015df78e"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java+//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository rules_java++toolchains+remotejdk11_linux_aarch64_toolchain_config_repo instantiated at:\n  <builtin>: in <toplevel>\nRepository rule _toolchain_config defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/rules_java+/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_java++toolchains+remotejdk11_linux_aarch64_toolchain_config_repo",
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_aarch64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_aarch64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java+//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "rules_java++toolchains+remotejdk11_linux_aarch64_toolchain_config_repo",
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_aarch64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_aarch64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "2e7db313a5a0ad282f0434887a5fde9eaa52368a0c6a5f2f92392975afdb488b"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java+//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository rules_java++toolchains+remotejdk11_linux_toolchain_config_repo instantiated at:\n  <builtin>: in <toplevel>\nRepository rule _toolchain_config defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/rules_java+/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_java++toolchains+remotejdk11_linux_toolchain_config_repo",
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java+//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "rules_java++toolchains+remotejdk11_linux_toolchain_config_repo",
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "7b065f02926480f4d598ad01766218e1f5e786506f80407f8ced66e7b3b711af"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java+//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository rules_java++toolchains+remote_jdk8_windows_toolchain_config_repo instantiated at:\n  <builtin>: in <toplevel>\nRepository rule _toolchain_config defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/rules_java+/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_java++toolchains+remote_jdk8_windows_toolchain_config_repo",
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_8\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"8\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_windows//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_windows//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java+//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "rules_java++toolchains+remote_jdk8_windows_toolchain_config_repo",
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_8\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"8\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_windows//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_windows//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "f5b38be3386bef11e817476fefb2849d178fbd79cf866074a7c437b09bbc9303"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java+//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository rules_java++toolchains+remote_jdk8_macos_aarch64_toolchain_config_repo instantiated at:\n  <builtin>: in <toplevel>\nRepository rule _toolchain_config defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/rules_java+/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_java++toolchains+remote_jdk8_macos_aarch64_toolchain_config_repo",
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_8\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"8\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_macos_aarch64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_macos_aarch64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java+//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "rules_java++toolchains+remote_jdk8_macos_aarch64_toolchain_config_repo",
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_8\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"8\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_macos_aarch64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_macos_aarch64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "1bcfd3f5d78042ea30fccbd9d204f44366f8904cb9bd50cc124f4dbad723b01a"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java+//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository rules_java++toolchains+remote_jdk8_macos_toolchain_config_repo instantiated at:\n  <builtin>: in <toplevel>\nRepository rule _toolchain_config defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/rules_java+/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_java++toolchains+remote_jdk8_macos_toolchain_config_repo",
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_8\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"8\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_macos//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_macos//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java+//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "rules_java++toolchains+remote_jdk8_macos_toolchain_config_repo",
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_8\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"8\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_macos//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_macos//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "6b1849c8189db5c16675f0727008dfe7c54c80cb19302df1bfbf5fdf633da0df"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java+//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository rules_java++toolchains+remote_jdk8_linux_s390x_toolchain_config_repo instantiated at:\n  <builtin>: in <toplevel>\nRepository rule _toolchain_config defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/rules_java+/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_java++toolchains+remote_jdk8_linux_s390x_toolchain_config_repo",
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_8\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"8\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_linux_s390x//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_linux_s390x//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java+//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "rules_java++toolchains+remote_jdk8_linux_s390x_toolchain_config_repo",
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_8\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"8\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_linux_s390x//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_linux_s390x//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "99b066fc10cd989363fd114619c545840978fa669b708e61a8a7b3a0b6bbb55c"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java+//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository rules_java++toolchains+remote_jdk8_linux_aarch64_toolchain_config_repo instantiated at:\n  <builtin>: in <toplevel>\nRepository rule _toolchain_config defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/rules_java+/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_java++toolchains+remote_jdk8_linux_aarch64_toolchain_config_repo",
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_8\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"8\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_linux_aarch64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_linux_aarch64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java+//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "rules_java++toolchains+remote_jdk8_linux_aarch64_toolchain_config_repo",
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_8\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"8\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_linux_aarch64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_linux_aarch64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "772b3a01b371f775211c77159cc56f7c910c053ffbf6dcd53fae642e80665fd4"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java+//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository rules_java++toolchains+remote_jdk8_linux_toolchain_config_repo instantiated at:\n  <builtin>: in <toplevel>\nRepository rule _toolchain_config defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/rules_java+/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_java++toolchains+remote_jdk8_linux_toolchain_config_repo",
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_8\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"8\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_linux//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_linux//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java+//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "rules_java++toolchains+remote_jdk8_linux_toolchain_config_repo",
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_8\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"8\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_linux//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_linux//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "25fdd6d185770a970e97754c5219cbec43d33c3bf0d274aa60786fba2c55ca01"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository apple_support+ instantiated at:\n  <builtin>: in <toplevel>\nRepository rule http_archive defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/bazel_tools/tools/build_defs/repo/http.bzl:431:31: in <toplevel>\n",
          "original_attributes": {
               "name": "apple_support+",
               "urls": [
                    "https://github.com/bazelbuild/apple_support/releases/download/1.23.1/apple_support.1.23.1.tar.gz"
               ],
               "integrity": "sha256-7iDMXAurRwZUc8gDPUYjdN040XJAbsyN5cjwhIeUPy8=",
               "strip_prefix": "",
               "remote_file_urls": {},
               "remote_file_integrity": {},
               "remote_module_file_urls": [
                    "https://bcr.bazel.build/modules/apple_support/1.23.1/MODULE.bazel"
               ],
               "remote_module_file_integrity": "sha256-U3Y/7UVqloz5GbMkBCfPOp1UgexUZqvJ1dxRvHAIdEI=",
               "remote_patches": {
                    "https://bcr.bazel.build/modules/apple_support/1.23.1/patches/module_dot_bazel_version.patch": "sha256-yqwfzmg9lIV674KI+GHtlok/967e8C2Ap8bPggzPm58="
               },
               "remote_patch_strip": 1
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "name": "apple_support+",
                         "urls": [
                              "https://github.com/bazelbuild/apple_support/releases/download/1.23.1/apple_support.1.23.1.tar.gz"
                         ],
                         "integrity": "sha256-7iDMXAurRwZUc8gDPUYjdN040XJAbsyN5cjwhIeUPy8=",
                         "strip_prefix": "",
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_module_file_urls": [
                              "https://bcr.bazel.build/modules/apple_support/1.23.1/MODULE.bazel"
                         ],
                         "remote_module_file_integrity": "sha256-U3Y/7UVqloz5GbMkBCfPOp1UgexUZqvJ1dxRvHAIdEI=",
                         "remote_patches": {
                              "https://bcr.bazel.build/modules/apple_support/1.23.1/patches/module_dot_bazel_version.patch": "sha256-yqwfzmg9lIV674KI+GHtlok/967e8C2Ap8bPggzPm58="
                         },
                         "remote_patch_strip": 1
                    },
                    "output_tree_hash": "8d0e1b8be326ebdfad3f69321077b6725c5f1a8b34ed855f6acffc4becbca8c6"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java+//toolchains:local_java_repository.bzl%_local_java_repository_rule",
          "definition_information": "Repository rules_java++toolchains+local_jdk instantiated at:\n  <builtin>: in <toplevel>\nRepository rule _local_java_repository_rule defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/rules_java+/toolchains/local_java_repository.bzl:297:46: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_java++toolchains+local_jdk",
               "runtime_name": "local_jdk",
               "build_file_content": "load(\"@rules_java//java/toolchains:java_runtime.bzl\", \"java_runtime\")\n\npackage(default_visibility = [\"//visibility:public\"])\n\nexports_files([\"WORKSPACE\", \"BUILD.bazel\"])\n\nfilegroup(\n    name = \"jre\",\n    srcs = glob(\n        [\n            \"jre/bin/**\",\n            \"jre/lib/**\",\n        ],\n        allow_empty = True,\n        # In some configurations, Java browser plugin is considered harmful and\n        # common antivirus software blocks access to npjp2.dll interfering with Bazel,\n        # so do not include it in JRE on Windows.\n        exclude = [\"jre/bin/plugin2/**\"],\n    ),\n)\n\nfilegroup(\n    name = \"jdk-bin\",\n    srcs = glob(\n        [\"bin/**\"],\n        # The JDK on Windows sometimes contains a directory called\n        # \"%systemroot%\", which is not a valid label.\n        exclude = [\"**/*%*/**\"],\n    ),\n)\n\n# This folder holds security policies.\nfilegroup(\n    name = \"jdk-conf\",\n    srcs = glob(\n        [\"conf/**\"],\n        allow_empty = True,\n    ),\n)\n\nfilegroup(\n    name = \"jdk-include\",\n    srcs = glob(\n        [\"include/**\"],\n        allow_empty = True,\n    ),\n)\n\nfilegroup(\n    name = \"jdk-lib\",\n    srcs = glob(\n        [\"lib/**\", \"release\"],\n        allow_empty = True,\n        exclude = [\n            \"lib/missioncontrol/**\",\n            \"lib/visualvm/**\",\n        ],\n    ),\n)\n\njava_runtime(\n    name = \"jdk\",\n    srcs = [\n        \":jdk-bin\",\n        \":jdk-conf\",\n        \":jdk-include\",\n        \":jdk-lib\",\n        \":jre\",\n    ],\n    # Provide the 'java` binary explicitly so that the correct path is used by\n    # Bazel even when the host platform differs from the execution platform.\n    # Exactly one of the two globs will be empty depending on the host platform.\n    # When --incompatible_disallow_empty_glob is enabled, each individual empty\n    # glob will fail without allow_empty = True, even if the overall result is\n    # non-empty.\n    java = glob([\"bin/java.exe\", \"bin/java\"], allow_empty = True)[0],\n    version = {RUNTIME_VERSION},\n)\n\nfilegroup(\n    name = \"jdk-jmods\",\n    srcs = glob(\n        [\"jmods/**\"],\n        allow_empty = True,\n    ),\n)\n\njava_runtime(\n    name = \"jdk-with-jmods\",\n    srcs = [\n        \":jdk-bin\",\n        \":jdk-conf\",\n        \":jdk-include\",\n        \":jdk-lib\",\n        \":jdk-jmods\",\n        \":jre\",\n    ],\n    java = glob([\"bin/java.exe\", \"bin/java\"], allow_empty = True)[0],\n    version = {RUNTIME_VERSION},\n)\n",
               "java_home": "",
               "version": ""
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java+//toolchains:local_java_repository.bzl%_local_java_repository_rule",
                    "attributes": {
                         "name": "rules_java++toolchains+local_jdk",
                         "runtime_name": "local_jdk",
                         "build_file_content": "load(\"@rules_java//java/toolchains:java_runtime.bzl\", \"java_runtime\")\n\npackage(default_visibility = [\"//visibility:public\"])\n\nexports_files([\"WORKSPACE\", \"BUILD.bazel\"])\n\nfilegroup(\n    name = \"jre\",\n    srcs = glob(\n        [\n            \"jre/bin/**\",\n            \"jre/lib/**\",\n        ],\n        allow_empty = True,\n        # In some configurations, Java browser plugin is considered harmful and\n        # common antivirus software blocks access to npjp2.dll interfering with Bazel,\n        # so do not include it in JRE on Windows.\n        exclude = [\"jre/bin/plugin2/**\"],\n    ),\n)\n\nfilegroup(\n    name = \"jdk-bin\",\n    srcs = glob(\n        [\"bin/**\"],\n        # The JDK on Windows sometimes contains a directory called\n        # \"%systemroot%\", which is not a valid label.\n        exclude = [\"**/*%*/**\"],\n    ),\n)\n\n# This folder holds security policies.\nfilegroup(\n    name = \"jdk-conf\",\n    srcs = glob(\n        [\"conf/**\"],\n        allow_empty = True,\n    ),\n)\n\nfilegroup(\n    name = \"jdk-include\",\n    srcs = glob(\n        [\"include/**\"],\n        allow_empty = True,\n    ),\n)\n\nfilegroup(\n    name = \"jdk-lib\",\n    srcs = glob(\n        [\"lib/**\", \"release\"],\n        allow_empty = True,\n        exclude = [\n            \"lib/missioncontrol/**\",\n            \"lib/visualvm/**\",\n        ],\n    ),\n)\n\njava_runtime(\n    name = \"jdk\",\n    srcs = [\n        \":jdk-bin\",\n        \":jdk-conf\",\n        \":jdk-include\",\n        \":jdk-lib\",\n        \":jre\",\n    ],\n    # Provide the 'java` binary explicitly so that the correct path is used by\n    # Bazel even when the host platform differs from the execution platform.\n    # Exactly one of the two globs will be empty depending on the host platform.\n    # When --incompatible_disallow_empty_glob is enabled, each individual empty\n    # glob will fail without allow_empty = True, even if the overall result is\n    # non-empty.\n    java = glob([\"bin/java.exe\", \"bin/java\"], allow_empty = True)[0],\n    version = {RUNTIME_VERSION},\n)\n\nfilegroup(\n    name = \"jdk-jmods\",\n    srcs = glob(\n        [\"jmods/**\"],\n        allow_empty = True,\n    ),\n)\n\njava_runtime(\n    name = \"jdk-with-jmods\",\n    srcs = [\n        \":jdk-bin\",\n        \":jdk-conf\",\n        \":jdk-include\",\n        \":jdk-lib\",\n        \":jdk-jmods\",\n        \":jre\",\n    ],\n    java = glob([\"bin/java.exe\", \"bin/java\"], allow_empty = True)[0],\n    version = {RUNTIME_VERSION},\n)\n",
                         "java_home": "",
                         "version": ""
                    },
                    "output_tree_hash": "be2ce6cc462a820437798e1664b8537ba207298137b779e98b90b896b93bde7b"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository rules_kotlin+ instantiated at:\n  <builtin>: in <toplevel>\nRepository rule http_archive defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/bazel_tools/tools/build_defs/repo/http.bzl:431:31: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_kotlin+",
               "urls": [
                    "https://github.com/bazelbuild/rules_kotlin/releases/download/v1.9.6/rules_kotlin-v1.9.6.tar.gz"
               ],
               "integrity": "sha256-O3cpdv7Hvc2h2EudObF2WJQkwEfrIXW+0JqsYw5Qr0M=",
               "strip_prefix": "",
               "remote_file_urls": {},
               "remote_file_integrity": {},
               "remote_module_file_urls": [
                    "https://bcr.bazel.build/modules/rules_kotlin/1.9.6/MODULE.bazel"
               ],
               "remote_module_file_integrity": "sha256-0mmgGhjudNAzVFCxD2LJ7YHyMh15WKKTTkQnL+gtzvM=",
               "remote_patches": {
                    "https://bcr.bazel.build/modules/rules_kotlin/1.9.6/patches/module_dot_bazel_version.patch": "sha256-DzcJ53CqDqD+AiboAl8Tq2/fKJRXn0g5O2g4UQfLrbE="
               },
               "remote_patch_strip": 1
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "name": "rules_kotlin+",
                         "urls": [
                              "https://github.com/bazelbuild/rules_kotlin/releases/download/v1.9.6/rules_kotlin-v1.9.6.tar.gz"
                         ],
                         "integrity": "sha256-O3cpdv7Hvc2h2EudObF2WJQkwEfrIXW+0JqsYw5Qr0M=",
                         "strip_prefix": "",
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_module_file_urls": [
                              "https://bcr.bazel.build/modules/rules_kotlin/1.9.6/MODULE.bazel"
                         ],
                         "remote_module_file_integrity": "sha256-0mmgGhjudNAzVFCxD2LJ7YHyMh15WKKTTkQnL+gtzvM=",
                         "remote_patches": {
                              "https://bcr.bazel.build/modules/rules_kotlin/1.9.6/patches/module_dot_bazel_version.patch": "sha256-DzcJ53CqDqD+AiboAl8Tq2/fKJRXn0g5O2g4UQfLrbE="
                         },
                         "remote_patch_strip": 1
                    },
                    "output_tree_hash": "7fdb8c7274faeacf51d25573c00b1c32e06f8901a27803e1290ae00e1b8ec935"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository rules_foreign_cc+ instantiated at:\n  <builtin>: in <toplevel>\nRepository rule http_archive defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/bazel_tools/tools/build_defs/repo/http.bzl:431:31: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_foreign_cc+",
               "urls": [
                    "https://github.com/bazelbuild/rules_foreign_cc/releases/download/0.10.1/rules_foreign_cc-0.10.1.tar.gz"
               ],
               "integrity": "sha256-R2MDvQ8bBMwxH8JY8XCKX274LTCR5T/Rl3+iA4NCWmo=",
               "strip_prefix": "rules_foreign_cc-0.10.1",
               "remote_file_urls": {},
               "remote_file_integrity": {},
               "remote_module_file_urls": [
                    "https://bcr.bazel.build/modules/rules_foreign_cc/0.10.1/MODULE.bazel"
               ],
               "remote_module_file_integrity": "sha256-uVJwEOX+8GCvkrZyTts2kZcKWx9290sh0599QzZBvmA=",
               "remote_patches": {
                    "https://bcr.bazel.build/modules/rules_foreign_cc/0.10.1/patches/module_dot_bazel.patch": "sha256-hDvLi+Nx91lvhEd2qRrPfPu0RjiG5w3a/c4N4AiJb3U="
               },
               "remote_patch_strip": 0
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "name": "rules_foreign_cc+",
                         "urls": [
                              "https://github.com/bazelbuild/rules_foreign_cc/releases/download/0.10.1/rules_foreign_cc-0.10.1.tar.gz"
                         ],
                         "integrity": "sha256-R2MDvQ8bBMwxH8JY8XCKX274LTCR5T/Rl3+iA4NCWmo=",
                         "strip_prefix": "rules_foreign_cc-0.10.1",
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_module_file_urls": [
                              "https://bcr.bazel.build/modules/rules_foreign_cc/0.10.1/MODULE.bazel"
                         ],
                         "remote_module_file_integrity": "sha256-uVJwEOX+8GCvkrZyTts2kZcKWx9290sh0599QzZBvmA=",
                         "remote_patches": {
                              "https://bcr.bazel.build/modules/rules_foreign_cc/0.10.1/patches/module_dot_bazel.patch": "sha256-hDvLi+Nx91lvhEd2qRrPfPu0RjiG5w3a/c4N4AiJb3U="
                         },
                         "remote_patch_strip": 0
                    },
                    "output_tree_hash": "cd7823ea631c6cb11aa47b8dae8cafea2063ac187b2f746c2402b40d23aee209"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_kotlin+//src/main/starlark/core/repositories:compiler.bzl%kotlin_capabilities_repository",
          "definition_information": "Repository rules_kotlin++rules_kotlin_extensions+com_github_jetbrains_kotlin instantiated at:\n  <builtin>: in <toplevel>\nRepository rule kotlin_capabilities_repository defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/rules_kotlin+/src/main/starlark/core/repositories/compiler.bzl:67:49: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_kotlin++rules_kotlin_extensions+com_github_jetbrains_kotlin",
               "git_repository_name": "com_github_jetbrains_kotlin_git",
               "compiler_version": "1.9.23"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_kotlin+//src/main/starlark/core/repositories:compiler.bzl%kotlin_capabilities_repository",
                    "attributes": {
                         "name": "rules_kotlin++rules_kotlin_extensions+com_github_jetbrains_kotlin",
                         "git_repository_name": "com_github_jetbrains_kotlin_git",
                         "compiler_version": "1.9.23"
                    },
                    "output_tree_hash": "53c782d82f328fde2439b58d4e9ff97843c011c93fbc89212a7f40f53f678b8a"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository rules_perl+ instantiated at:\n  <builtin>: in <toplevel>\nRepository rule http_archive defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/bazel_tools/tools/build_defs/repo/http.bzl:431:31: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_perl+",
               "urls": [
                    "https://github.com/bazel-contrib/rules_perl/archive/refs/tags/0.2.4.tar.gz"
               ],
               "integrity": "sha256-vHVQ84gfYyVaZcbex86Dw14K5I17mqfm6SN7BnM8v/g=",
               "strip_prefix": "rules_perl-0.2.4",
               "remote_file_urls": {},
               "remote_file_integrity": {},
               "remote_module_file_urls": [
                    "https://bcr.bazel.build/modules/rules_perl/0.2.4/MODULE.bazel"
               ],
               "remote_module_file_integrity": "sha256-X1r3vkv1+4jZGvdGlRjw/SFhcYrvxgYYj3zVH0NsqTg=",
               "remote_patches": {
                    "https://bcr.bazel.build/modules/rules_perl/0.2.4/patches/module_dot_bazel_version.patch": "sha256-pNzMxPUBCZaEvGJNW2eZR8X8UoF/pAYzrn/OC7/Fbmg="
               },
               "remote_patch_strip": 0
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "name": "rules_perl+",
                         "urls": [
                              "https://github.com/bazel-contrib/rules_perl/archive/refs/tags/0.2.4.tar.gz"
                         ],
                         "integrity": "sha256-vHVQ84gfYyVaZcbex86Dw14K5I17mqfm6SN7BnM8v/g=",
                         "strip_prefix": "rules_perl-0.2.4",
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_module_file_urls": [
                              "https://bcr.bazel.build/modules/rules_perl/0.2.4/MODULE.bazel"
                         ],
                         "remote_module_file_integrity": "sha256-X1r3vkv1+4jZGvdGlRjw/SFhcYrvxgYYj3zVH0NsqTg=",
                         "remote_patches": {
                              "https://bcr.bazel.build/modules/rules_perl/0.2.4/patches/module_dot_bazel_version.patch": "sha256-pNzMxPUBCZaEvGJNW2eZR8X8UoF/pAYzrn/OC7/Fbmg="
                         },
                         "remote_patch_strip": 0
                    },
                    "output_tree_hash": "38ef4482c772c859c1aa1f53461f24df3f57b7e6da6caac74fedaa0a626a6326"
               }
          ]
     },
     {
          "original_rule_class": "@@apple_support+//crosstool:setup_internal.bzl%apple_cc_autoconf_toolchains",
          "definition_information": "Repository apple_support++apple_cc_configure_extension+local_config_apple_cc_toolchains instantiated at:\n  <builtin>: in <toplevel>\nRepository rule apple_cc_autoconf_toolchains defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/apple_support+/crosstool/setup_internal.bzl:32:47: in <toplevel>\n",
          "original_attributes": {
               "name": "apple_support++apple_cc_configure_extension+local_config_apple_cc_toolchains"
          },
          "repositories": [
               {
                    "rule_class": "@@apple_support+//crosstool:setup_internal.bzl%apple_cc_autoconf_toolchains",
                    "attributes": {
                         "name": "apple_support++apple_cc_configure_extension+local_config_apple_cc_toolchains"
                    },
                    "output_tree_hash": "d5527625a3290689b9dcde30ea50ab1e6188173e312bc3810735c521806720b8"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_foreign_cc+//toolchains:prebuilt_toolchains_repository.bzl%prebuilt_toolchains_repository",
          "definition_information": "Repository rules_foreign_cc++tools+ninja_1.11.1_toolchains instantiated at:\n  <builtin>: in <toplevel>\nRepository rule prebuilt_toolchains_repository defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/rules_foreign_cc+/toolchains/prebuilt_toolchains_repository.bzl:58:49: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_foreign_cc++tools+ninja_1.11.1_toolchains",
               "repos": {
                    "ninja_1.11.1_linux": [
                         "@platforms//cpu:x86_64",
                         "@platforms//os:linux"
                    ],
                    "ninja_1.11.1_mac": [
                         "@platforms//cpu:x86_64",
                         "@platforms//os:macos"
                    ],
                    "ninja_1.11.1_win": [
                         "@platforms//cpu:x86_64",
                         "@platforms//os:windows"
                    ]
               },
               "tool": "ninja"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_foreign_cc+//toolchains:prebuilt_toolchains_repository.bzl%prebuilt_toolchains_repository",
                    "attributes": {
                         "name": "rules_foreign_cc++tools+ninja_1.11.1_toolchains",
                         "repos": {
                              "ninja_1.11.1_linux": [
                                   "@platforms//cpu:x86_64",
                                   "@platforms//os:linux"
                              ],
                              "ninja_1.11.1_mac": [
                                   "@platforms//cpu:x86_64",
                                   "@platforms//os:macos"
                              ],
                              "ninja_1.11.1_win": [
                                   "@platforms//cpu:x86_64",
                                   "@platforms//os:windows"
                              ]
                         },
                         "tool": "ninja"
                    },
                    "output_tree_hash": "d403d040bdd5d6db10857266bb7e6f6acf164f3442aa626bdc50c57e0660b984"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_foreign_cc+//foreign_cc/private/framework:toolchain.bzl%framework_toolchain_repository_hub",
          "definition_information": "Repository rules_foreign_cc++tools+rules_foreign_cc_framework_toolchains instantiated at:\n  <builtin>: in <toplevel>\nRepository rule framework_toolchain_repository_hub defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/rules_foreign_cc+/foreign_cc/private/framework/toolchain.bzl:85:53: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_foreign_cc++tools+rules_foreign_cc_framework_toolchains"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_foreign_cc+//foreign_cc/private/framework:toolchain.bzl%framework_toolchain_repository_hub",
                    "attributes": {
                         "name": "rules_foreign_cc++tools+rules_foreign_cc_framework_toolchains"
                    },
                    "output_tree_hash": "fa77c9978ac23aa3ea7523ee8970ad655992db2d9aba7a7403c671596a88fab3"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_foreign_cc+//toolchains:prebuilt_toolchains_repository.bzl%prebuilt_toolchains_repository",
          "definition_information": "Repository rules_foreign_cc++tools+cmake_3.23.2_toolchains instantiated at:\n  <builtin>: in <toplevel>\nRepository rule prebuilt_toolchains_repository defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/rules_foreign_cc+/toolchains/prebuilt_toolchains_repository.bzl:58:49: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_foreign_cc++tools+cmake_3.23.2_toolchains",
               "repos": {
                    "cmake-3.23.2-linux-aarch64": [
                         "@platforms//cpu:aarch64",
                         "@platforms//os:linux"
                    ],
                    "cmake-3.23.2-linux-x86_64": [
                         "@platforms//cpu:x86_64",
                         "@platforms//os:linux"
                    ],
                    "cmake-3.23.2-macos-universal": [
                         "@platforms//os:macos"
                    ],
                    "cmake-3.23.2-windows-i386": [
                         "@platforms//cpu:x86_32",
                         "@platforms//os:windows"
                    ],
                    "cmake-3.23.2-windows-x86_64": [
                         "@platforms//cpu:x86_64",
                         "@platforms//os:windows"
                    ]
               },
               "tool": "cmake"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_foreign_cc+//toolchains:prebuilt_toolchains_repository.bzl%prebuilt_toolchains_repository",
                    "attributes": {
                         "name": "rules_foreign_cc++tools+cmake_3.23.2_toolchains",
                         "repos": {
                              "cmake-3.23.2-linux-aarch64": [
                                   "@platforms//cpu:aarch64",
                                   "@platforms//os:linux"
                              ],
                              "cmake-3.23.2-linux-x86_64": [
                                   "@platforms//cpu:x86_64",
                                   "@platforms//os:linux"
                              ],
                              "cmake-3.23.2-macos-universal": [
                                   "@platforms//os:macos"
                              ],
                              "cmake-3.23.2-windows-i386": [
                                   "@platforms//cpu:x86_32",
                                   "@platforms//os:windows"
                              ],
                              "cmake-3.23.2-windows-x86_64": [
                                   "@platforms//cpu:x86_64",
                                   "@platforms//os:windows"
                              ]
                         },
                         "tool": "cmake"
                    },
                    "output_tree_hash": "7c1d4d447542e3cd7477bd39b570b39131dac64aca05df87e0f27513f628d12d"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository rules_go+ instantiated at:\n  <builtin>: in <toplevel>\nRepository rule http_archive defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/bazel_tools/tools/build_defs/repo/http.bzl:431:31: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_go+",
               "urls": [
                    "https://github.com/bazelbuild/rules_go/releases/download/v0.50.1/rules_go-v0.50.1.zip"
               ],
               "integrity": "sha256-9KkxRRjKas+hbMSrQ7C4zh5OpkuBw42KN3KIPxUzRrg=",
               "strip_prefix": "",
               "remote_file_urls": {},
               "remote_file_integrity": {},
               "remote_module_file_urls": [
                    "https://bcr.bazel.build/modules/rules_go/0.50.1/MODULE.bazel"
               ],
               "remote_module_file_integrity": "sha256-uRowjcV4K7CoAhrUMwyB/qW9p3+WueTBF7m5yPZmXuA=",
               "remote_patches": {},
               "remote_patch_strip": 0
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "name": "rules_go+",
                         "urls": [
                              "https://github.com/bazelbuild/rules_go/releases/download/v0.50.1/rules_go-v0.50.1.zip"
                         ],
                         "integrity": "sha256-9KkxRRjKas+hbMSrQ7C4zh5OpkuBw42KN3KIPxUzRrg=",
                         "strip_prefix": "",
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_module_file_urls": [
                              "https://bcr.bazel.build/modules/rules_go/0.50.1/MODULE.bazel"
                         ],
                         "remote_module_file_integrity": "sha256-uRowjcV4K7CoAhrUMwyB/qW9p3+WueTBF7m5yPZmXuA=",
                         "remote_patches": {},
                         "remote_patch_strip": 0
                    },
                    "output_tree_hash": "b953199259e8df7e47062abf808a16656f1dd4d75f7ca752459a22ace5e432e2"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_go+//go/private:sdk.bzl%go_multiple_toolchains",
          "definition_information": "Repository rules_go++go_sdk+go_toolchains instantiated at:\n  <builtin>: in <toplevel>\nRepository rule go_multiple_toolchains defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/rules_go+/go/private/sdk.bzl:294:41: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_go++go_sdk+go_toolchains",
               "prefixes": [
                    "_0000_protoc-gen-validate__download_0_",
                    "_0001_protoc-gen-validate__download_0_darwin_amd64_",
                    "_0002_protoc-gen-validate__download_0_darwin_arm64_",
                    "_0003_protoc-gen-validate__download_0_linux_amd64_",
                    "_0004_protoc-gen-validate__download_0_linux_arm64_",
                    "_0005_protoc-gen-validate__download_0_windows_arm64_",
                    "_0006_xds__download_0_",
                    "_0007_xds__download_0_darwin_amd64_",
                    "_0008_xds__download_0_darwin_arm64_",
                    "_0009_xds__download_0_linux_amd64_",
                    "_0010_xds__download_0_linux_arm64_",
                    "_0011_xds__download_0_windows_arm64_",
                    "_0012_go_default_sdk_",
                    "_0013_rules_go__download_0_darwin_amd64_",
                    "_0014_rules_go__download_0_darwin_arm64_",
                    "_0015_rules_go__download_0_linux_amd64_",
                    "_0016_rules_go__download_0_linux_arm64_",
                    "_0017_rules_go__download_0_windows_arm64_",
                    "_0018_cel-spec__download_0_",
                    "_0019_cel-spec__download_0_darwin_amd64_",
                    "_0020_cel-spec__download_0_darwin_arm64_",
                    "_0021_cel-spec__download_0_linux_amd64_",
                    "_0022_cel-spec__download_0_linux_arm64_",
                    "_0023_cel-spec__download_0_windows_arm64_"
               ],
               "sdk_repos": [
                    "protoc-gen-validate__download_0",
                    "protoc-gen-validate__download_0_darwin_amd64",
                    "protoc-gen-validate__download_0_darwin_arm64",
                    "protoc-gen-validate__download_0_linux_amd64",
                    "protoc-gen-validate__download_0_linux_arm64",
                    "protoc-gen-validate__download_0_windows_arm64",
                    "xds__download_0",
                    "xds__download_0_darwin_amd64",
                    "xds__download_0_darwin_arm64",
                    "xds__download_0_linux_amd64",
                    "xds__download_0_linux_arm64",
                    "xds__download_0_windows_arm64",
                    "go_default_sdk",
                    "rules_go__download_0_darwin_amd64",
                    "rules_go__download_0_darwin_arm64",
                    "rules_go__download_0_linux_amd64",
                    "rules_go__download_0_linux_arm64",
                    "rules_go__download_0_windows_arm64",
                    "cel-spec__download_0",
                    "cel-spec__download_0_darwin_amd64",
                    "cel-spec__download_0_darwin_arm64",
                    "cel-spec__download_0_linux_amd64",
                    "cel-spec__download_0_linux_arm64",
                    "cel-spec__download_0_windows_arm64"
               ],
               "sdk_types": [
                    "remote",
                    "remote",
                    "remote",
                    "remote",
                    "remote",
                    "remote",
                    "remote",
                    "remote",
                    "remote",
                    "remote",
                    "remote",
                    "remote",
                    "remote",
                    "remote",
                    "remote",
                    "remote",
                    "remote",
                    "remote",
                    "remote",
                    "remote",
                    "remote",
                    "remote",
                    "remote",
                    "remote"
               ],
               "sdk_versions": [
                    "1.21.1",
                    "1.21.1",
                    "1.21.1",
                    "1.21.1",
                    "1.21.1",
                    "1.21.1",
                    "1.20.2",
                    "1.20.2",
                    "1.20.2",
                    "1.20.2",
                    "1.20.2",
                    "1.20.2",
                    "1.21.8",
                    "1.21.8",
                    "1.21.8",
                    "1.21.8",
                    "1.21.8",
                    "1.21.8",
                    "1.19.1",
                    "1.19.1",
                    "1.19.1",
                    "1.19.1",
                    "1.19.1",
                    "1.19.1"
               ],
               "geese": [
                    "",
                    "darwin",
                    "darwin",
                    "linux",
                    "linux",
                    "windows",
                    "",
                    "darwin",
                    "darwin",
                    "linux",
                    "linux",
                    "windows",
                    "",
                    "darwin",
                    "darwin",
                    "linux",
                    "linux",
                    "windows",
                    "",
                    "darwin",
                    "darwin",
                    "linux",
                    "linux",
                    "windows"
               ],
               "goarchs": [
                    "",
                    "amd64",
                    "arm64",
                    "amd64",
                    "arm64",
                    "arm64",
                    "",
                    "amd64",
                    "arm64",
                    "amd64",
                    "arm64",
                    "arm64",
                    "",
                    "amd64",
                    "arm64",
                    "amd64",
                    "arm64",
                    "arm64",
                    "",
                    "amd64",
                    "arm64",
                    "amd64",
                    "arm64",
                    "arm64"
               ]
          },
          "repositories": [
               {
                    "rule_class": "@@rules_go+//go/private:sdk.bzl%go_multiple_toolchains",
                    "attributes": {
                         "name": "rules_go++go_sdk+go_toolchains",
                         "prefixes": [
                              "_0000_protoc-gen-validate__download_0_",
                              "_0001_protoc-gen-validate__download_0_darwin_amd64_",
                              "_0002_protoc-gen-validate__download_0_darwin_arm64_",
                              "_0003_protoc-gen-validate__download_0_linux_amd64_",
                              "_0004_protoc-gen-validate__download_0_linux_arm64_",
                              "_0005_protoc-gen-validate__download_0_windows_arm64_",
                              "_0006_xds__download_0_",
                              "_0007_xds__download_0_darwin_amd64_",
                              "_0008_xds__download_0_darwin_arm64_",
                              "_0009_xds__download_0_linux_amd64_",
                              "_0010_xds__download_0_linux_arm64_",
                              "_0011_xds__download_0_windows_arm64_",
                              "_0012_go_default_sdk_",
                              "_0013_rules_go__download_0_darwin_amd64_",
                              "_0014_rules_go__download_0_darwin_arm64_",
                              "_0015_rules_go__download_0_linux_amd64_",
                              "_0016_rules_go__download_0_linux_arm64_",
                              "_0017_rules_go__download_0_windows_arm64_",
                              "_0018_cel-spec__download_0_",
                              "_0019_cel-spec__download_0_darwin_amd64_",
                              "_0020_cel-spec__download_0_darwin_arm64_",
                              "_0021_cel-spec__download_0_linux_amd64_",
                              "_0022_cel-spec__download_0_linux_arm64_",
                              "_0023_cel-spec__download_0_windows_arm64_"
                         ],
                         "sdk_repos": [
                              "protoc-gen-validate__download_0",
                              "protoc-gen-validate__download_0_darwin_amd64",
                              "protoc-gen-validate__download_0_darwin_arm64",
                              "protoc-gen-validate__download_0_linux_amd64",
                              "protoc-gen-validate__download_0_linux_arm64",
                              "protoc-gen-validate__download_0_windows_arm64",
                              "xds__download_0",
                              "xds__download_0_darwin_amd64",
                              "xds__download_0_darwin_arm64",
                              "xds__download_0_linux_amd64",
                              "xds__download_0_linux_arm64",
                              "xds__download_0_windows_arm64",
                              "go_default_sdk",
                              "rules_go__download_0_darwin_amd64",
                              "rules_go__download_0_darwin_arm64",
                              "rules_go__download_0_linux_amd64",
                              "rules_go__download_0_linux_arm64",
                              "rules_go__download_0_windows_arm64",
                              "cel-spec__download_0",
                              "cel-spec__download_0_darwin_amd64",
                              "cel-spec__download_0_darwin_arm64",
                              "cel-spec__download_0_linux_amd64",
                              "cel-spec__download_0_linux_arm64",
                              "cel-spec__download_0_windows_arm64"
                         ],
                         "sdk_types": [
                              "remote",
                              "remote",
                              "remote",
                              "remote",
                              "remote",
                              "remote",
                              "remote",
                              "remote",
                              "remote",
                              "remote",
                              "remote",
                              "remote",
                              "remote",
                              "remote",
                              "remote",
                              "remote",
                              "remote",
                              "remote",
                              "remote",
                              "remote",
                              "remote",
                              "remote",
                              "remote",
                              "remote"
                         ],
                         "sdk_versions": [
                              "1.21.1",
                              "1.21.1",
                              "1.21.1",
                              "1.21.1",
                              "1.21.1",
                              "1.21.1",
                              "1.20.2",
                              "1.20.2",
                              "1.20.2",
                              "1.20.2",
                              "1.20.2",
                              "1.20.2",
                              "1.21.8",
                              "1.21.8",
                              "1.21.8",
                              "1.21.8",
                              "1.21.8",
                              "1.21.8",
                              "1.19.1",
                              "1.19.1",
                              "1.19.1",
                              "1.19.1",
                              "1.19.1",
                              "1.19.1"
                         ],
                         "geese": [
                              "",
                              "darwin",
                              "darwin",
                              "linux",
                              "linux",
                              "windows",
                              "",
                              "darwin",
                              "darwin",
                              "linux",
                              "linux",
                              "windows",
                              "",
                              "darwin",
                              "darwin",
                              "linux",
                              "linux",
                              "windows",
                              "",
                              "darwin",
                              "darwin",
                              "linux",
                              "linux",
                              "windows"
                         ],
                         "goarchs": [
                              "",
                              "amd64",
                              "arm64",
                              "amd64",
                              "arm64",
                              "arm64",
                              "",
                              "amd64",
                              "arm64",
                              "amd64",
                              "arm64",
                              "arm64",
                              "",
                              "amd64",
                              "arm64",
                              "amd64",
                              "arm64",
                              "arm64",
                              "",
                              "amd64",
                              "arm64",
                              "amd64",
                              "arm64",
                              "arm64"
                         ]
                    },
                    "output_tree_hash": "24a0d62f3335813a59bec6b853bf03a89d60948fcf79e2f53d6c93f29d752626"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_go+//go/private:nogo.bzl%go_register_nogo",
          "definition_information": "Repository rules_go++go_sdk+io_bazel_rules_nogo instantiated at:\n  <builtin>: in <toplevel>\nRepository rule go_register_nogo defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/rules_go+/go/private/nogo.bzl:54:35: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_go++go_sdk+io_bazel_rules_nogo",
               "nogo": "@io_bazel_rules_go//:default_nogo",
               "includes": [
                    "@@//:__subpackages__"
               ],
               "excludes": []
          },
          "repositories": [
               {
                    "rule_class": "@@rules_go+//go/private:nogo.bzl%go_register_nogo",
                    "attributes": {
                         "name": "rules_go++go_sdk+io_bazel_rules_nogo",
                         "nogo": "@io_bazel_rules_go//:default_nogo",
                         "includes": [
                              "@@//:__subpackages__"
                         ],
                         "excludes": []
                    },
                    "output_tree_hash": "d613bc7e959e31ca7385fe86cfe454c30a777567c76929528c61abdb6a418ed1"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_cc+//cc/private/toolchain:cc_configure.bzl%cc_autoconf",
          "definition_information": "Repository rules_cc++cc_configure_extension+local_config_cc instantiated at:\n  <builtin>: in <toplevel>\nRepository rule cc_autoconf defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/rules_cc+/cc/private/toolchain/cc_configure.bzl:109:30: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_cc++cc_configure_extension+local_config_cc"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_cc+//cc/private/toolchain:cc_configure.bzl%cc_autoconf",
                    "attributes": {
                         "name": "rules_cc++cc_configure_extension+local_config_cc"
                    },
                    "output_tree_hash": "67de39411bcfb9ba363deae3557fbc8de480a8368e981697bd8d211745a0994c"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository abseil-cpp+ instantiated at:\n  <builtin>: in <toplevel>\nRepository rule http_archive defined at:\n  C:/users/gebruiker/_bazel_gebruiker/up3epz4i/external/bazel_tools/tools/build_defs/repo/http.bzl:431:31: in <toplevel>\n",
          "original_attributes": {
               "name": "abseil-cpp+",
               "urls": [
                    "https://github.com/abseil/abseil-cpp/releases/download/20250127.1/abseil-cpp-20250127.1.tar.gz"
               ],
               "integrity": "sha256-s5ZAH9KeLmecrOd4Z0gdOIyAdnHcKsxgKgJZ7rebeBE=",
               "strip_prefix": "abseil-cpp-20250127.1",
               "remote_file_urls": {},
               "remote_file_integrity": {},
               "remote_module_file_urls": [
                    "https://bcr.bazel.build/modules/abseil-cpp/20250127.1/MODULE.bazel"
               ],
               "remote_module_file_integrity": "sha256-xKiefOub8eJc+Eqfgw/2uBe3KHQIi/UUGzFHJuRqV8E=",
               "remote_patches": {},
               "remote_patch_strip": 0
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "name": "abseil-cpp+",
                         "urls": [
                              "https://github.com/abseil/abseil-cpp/releases/download/20250127.1/abseil-cpp-20250127.1.tar.gz"
                         ],
                         "integrity": "sha256-s5ZAH9KeLmecrOd4Z0gdOIyAdnHcKsxgKgJZ7rebeBE=",
                         "strip_prefix": "abseil-cpp-20250127.1",
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_module_file_urls": [
                              "https://bcr.bazel.build/modules/abseil-cpp/20250127.1/MODULE.bazel"
                         ],
                         "remote_module_file_integrity": "sha256-xKiefOub8eJc+Eqfgw/2uBe3KHQIi/UUGzFHJuRqV8E=",
                         "remote_patches": {},
                         "remote_patch_strip": 0
                    },
                    "output_tree_hash": "cd89be9903c655d5080a572f9975262608e3bb9041dced2132e4b12de7557f52"
               }
          ]
     }
]