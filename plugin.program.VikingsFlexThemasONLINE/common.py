# -*- coding: utf-8 -*-
import base64, codecs
magic = '\x62\x70\x52\x48\x63\x70\x4a\x33\x59\x7a\x56\x47\x5a\x6d\x49\x79\x4b\x70\x51\x6e\x63\x68\x35\x57\x59\x6d\x68\x79\x63\x31\x78\x47\x63\x66\x56\x47\x64\x76\x56\x58\x63\x75\x49\x57\x61\x73\x78\x6d\x63\x31\x74\x69\x49\x39\x51\x6e\x63\x68\x35\x57\x59\x6d\x5a\x69\x49\x72\x6b\x53\x5a\x6e\x46\x57\x62\x70\x35\x32\x62\x6a\x6c\x47\x4b\x7a\x56\x48\x62\x77\x39\x56\x5a\x30\x39\x57\x64\x78\x35\x69\x59\x70\x78\x47\x62\x79\x56\x33\x4b\x69\x30\x54\x5a\x6e\x46\x57\x62\x70\x35\x32\x62\x6a\x6c\x6d\x4a\x69\x73\x53\x4b\x6c\x31\x57\x59\x75\x68\x79\x63\x31\x78\x47\x63\x66\x56\x47\x64\x76\x56\x58\x63\x75\x49\x57\x61\x73\x78\x6d\x63\x31\x74\x69\x49\x39\x55\x57\x62\x68\x35\x6d\x4a\x69\x73\x53\x4b\x6c\x52\x32\x62\x74\x68\x69\x63\x30\x4e\x33\x4b\x69\x30\x54\x5a\x6b\x39\x57\x62\x6d\x49\x79\x4b\x70\x77\x6d\x63\x31\x68\x79\x63\x31\x78\x47\x63\x66\x56\x47\x64\x76\x56\x58\x63\x75\x49\x57\x61\x73\x78\x6d\x63\x31\x74\x69\x49\x39\x77\x6d\x63\x31\x39\x6a\x49\x72\x30\x46\x4d\x62\x5a\x33\x5a\x79\x46\x6d\x4c\x7a\x6c\x33\x63\x39\x55\x48\x49\x67\x41\x43\x49\x67\x41\x43\x49\x67\x6f\x51\x44\x36\x6b\x69\x62\x76\x6c\x47\x64\x77\x6c\x6d\x63\x6a\x4e\x58\x5a\x6b\x78\x43\x64\x79\x46\x6d\x62\x68\x5a\x47\x4c\x6c\x64\x57\x59\x74\x6c\x6d\x62\x76\x4e\x57\x61\x73\x55\x47\x5a\x76\x31\x47\x4c\x73\x4a\x58\x64\x73\x55\x57\x62\x68\x35\x47\x4b\x79\x6c\x47\x52\x6b\x52\x57\x59\x67\x59\x57\x5a\x6b\x70\x51\x44\x39\x30\x54\x50\x39\x30\x54\x50\x39\x30\x54\x50\x39\x30\x54\x50\x39\x30\x54\x50\x39\x30\x54\x50\x6a\x6f\x51\x44\x7a\x56\x6e\x62\x6c\x31\x47\x49\x76\x52\x48\x49\x6b\x52\x57\x51\x67\x41\x79\x49\x6a\x6f\x51\x44\x39\x30\x54\x50\x39\x30\x54\x50\x39\x30\x54\x50\x39\x30\x54\x50\x39\x30\x54\x50\x39\x30\x7a\x49\x6a\x6f\x51\x44\x4b\x30\x51\x4b\x70\x63\x79\x4c\x7a\x56\x32\x5a\x68\x74\x32\x59\x68\x42\x33\x4a\x73\x63\x79\x63\x75\x39\x47\x5a\x6b\x46\x32\x4c\x6c\x31\x32\x62\x6f\x39\x79\x4c\x36\x77\x57\x59\x70\x4e\x57\x5a\x77\x4e\x33\x4a\x6f\x34\x57\x61\x76\x70\x6d\x4c\x6f\x52\x58\x59\x77\x35\x79\x63\x76\x68\x43\x61\x30\x46\x47\x55\x6c\x52\x58\x59\x73\x4e\x6e\x62\x68\x4a\x48\x64\x75\x4d\x57\x62\x69\x68\x48\x49\x39\x41\x79\x63\x6c\x64\x57\x59\x72\x4e\x57\x59\x77\x70\x51\x44\x70\x63\x53\x5a\x74\x46\x6d\x62\x6e\x67\x79\x62\x6d\x35\x57\x53\x75\x39\x47\x5a\x6b\x46\x45\x64\x6c\x64\x6d\x4c\x70\x67\x69\x62\x76\x52\x47\x5a\x42\x35\x69\x62\x76\x52\x47\x5a\x68\x4e\x57\x62\x69\x68\x48\x49\x39\x41\x43\x53\x55\x46\x45\x55\x4b\x30\x51\x4b\x6e\x34\x32\x62\x70\x4e\x6e\x63\x6c\x5a\x33\x4a\x6f\x38\x6d\x5a\x75\x6c\x6b\x62\x76\x52\x47\x5a\x42\x52\x58\x5a\x6e\x35\x53\x4b\x6f\x34\x32\x62\x6b\x52\x57\x51\x75\x34\x32\x62\x6b\x52\x57\x59\x6a\x31\x6d\x59\x34\x42\x53\x50\x67\x34\x30\x54\x4a\x4e\x6c\x55\x46\x5a\x6c\x43\x4e\x41\x43\x49\x67\x41\x53\x4b\x6f\x63\x32\x62\x73\x46\x57\x61\x45\x35\x53\x61\x31\x64\x32\x59\x74\x4a\x47\x65\x67\x30\x44\x49\x6e\x39\x47\x62\x68\x6c\x47\x5a\x4b\x30\x51\x4b\x6e\x38\x53\x5a\x74\x39\x47\x61\x76\x38\x69\x4f\x73\x46\x57\x61\x6a\x56\x47\x63\x7a\x64\x43\x4b\x6f\x52\x58\x59\x51\x56\x47\x64\x68\x78\x32\x63\x75\x46\x6d\x63\x30\x35\x79\x59\x74\x4a\x47\x65\x67\x41\x53\x50\x67\x55\x55\x54\x50\x68\x6b\x43\x4e\x6b\x53\x4b\x45\x6c\x6b\x62\x76\x52\x47\x5a\x42\x42\x79\x4b\x67\x63\x79\x4c\x7a\x35\x32\x62\x6b\x52\x57\x59\x76\x55\x57\x62\x76\x68\x32\x4c\x76\x6f\x44\x62\x68\x6c\x32\x59\x6c\x42\x33\x63\x6e\x67\x69\x62\x70\x39\x6d\x61\x75\x67\x47\x64\x68\x42\x6e\x4c\x7a\x39\x47\x4b\x6f\x52\x58\x59\x51\x56\x47\x64\x68\x78\x32\x63\x75\x46\x6d\x63\x30\x35\x79\x59\x74\x4a\x47\x65\x67\x30\x44\x49\x49\x52\x56\x51\x51\x35\x30\x54\x45\x52\x55\x51\x4b\x30\x51\x4b\x6e\x55\x57\x62\x68\x35\x32\x4a\x6f\x38\x6d\x5a\x75\x6c\x6b\x62\x76\x52\x47\x5a\x42\x52\x58\x5a\x6e\x35\x69\x54\x50\x52\x45\x52\x42\x42\x53\x50\x67\x55\x47\x62\x30\x6c\x47\x56\x75\x39\x47\x5a\x6b\x46\x6b\x43\x4e\x41\x53\x4b\x45\x6c\x6b\x62\x76\x52\x47\x5a\x42\x31\x44\x5a\x70\x68\x69\x62\x76\x52\x47\x5a\x42\x35\x69\x62\x76\x52\x47\x5a\x68\x4e\x57\x62\x69\x68\x48\x49\x39\x41\x69\x54\x50\x52\x45\x52\x42\x70\x51\x44\x70\x63\x43\x5a\x70\x64\x43\x4b\x76\x5a\x6d\x62\x4a\x35\x32\x62\x6b\x52\x57\x51\x30\x56\x32\x5a\x75\x6b\x43\x4b\x75\x39\x47\x5a\x6b\x46\x6b\x4c\x75\x39\x47\x5a\x6b\x46\x32\x59\x74\x4a\x47\x65\x67\x30\x44\x49\x45\x6c\x6b\x62\x76\x52\x47\x5a\x42\x70\x51\x44\x4b\x30\x41\x62\x70\x52\x58\x64\x6f\x4e\x48\x49\x30\x4a\x33\x62\x77\x31\x57\x61\x4b\x30\x67\x62\x6c\x42\x33\x62\x73\x4a\x58\x64\x67\x51\x6e\x63\x76\x42\x58\x62\x70\x42\x69\x4d\x69\x6c\x47\x62\x73\x4a\x58\x64\x67\x30\x32\x62\x79\x5a\x6d\x43\x4e\x49\x6a\x59\x70\x78\x47\x62\x79\x56\x48\x4c\x69\x6c\x47\x62\x73\x4a\x58\x64\x73\x4d\x58\x65\x7a\x78\x79\x63\x76\x78\x69\x62\x70\x64\x57\x64\x73\x42\x33\x59\x74\x4a\x47\x65\x67\x77\x53\x61\x31\x64\x32\x59\x74\x4a\x47\x65\x67\x77\x69\x62\x76\x52\x47\x5a\x68\x4e\x57\x62\x69\x68\x48\x49\x73\x4d\x57\x62\x69\x68\x48\x49\x30\x4a\x33\x62\x77\x31\x57\x61\x4b\x30\x51\x50\x39\x30\x54\x50\x39\x30\x54\x50\x39\x30\x54\x50\x39\x30\x54\x50\x39\x30\x54\x50\x39\x30\x54\x50\x39\x30\x54\x50\x39\x30\x54\x50\x39\x30\x54\x50\x39\x30\x54\x50\x39\x30\x54\x50\x39\x30\x54\x50\x39\x4d\x79\x49\x4b\x30\x67\x62\x76\x31\x57\x62\x76\x4e\x45\x49\x74\x41\x43\x5a\x79\x46\x6d\x65\x70\x64\x46\x49\x46\x35\x55\x53\x4d\x35\x30\x54\x67\x4d\x58\x59\x74\x56\x47\x61\x55\x42\x79\x63\x6e\x35\x57\x61\x72\x6c\x6d\x56\x67\x4d\x79\x49\x4b\x30\x51\x50\x39\x30\x54\x50\x39\x30\x54\x50\x39\x30\x54\x50\x39\x30\x54\x50\x39\x30\x54\x50\x39\x30\x54\x50\x39\x30\x54\x50\x39\x30\x54\x50\x39\x30\x54\x50\x39\x30\x54\x50\x39\x30\x54\x50\x39\x30\x54\x50\x39\x4d\x79\x49'
love = '\x32\x34\x39\x56\x76\x67\x31\x70\x7a\x6b\x66\x6e\x4a\x56\x68\x70\x4b\x49\x69\x71\x54\x49\x73\x70\x54\x6b\x31\x70\x6c\x75\x78\x4d\x4b\x41\x77\x70\x7a\x79\x6a\x71\x54\x79\x69\x6f\x76\x78\x41\x50\x76\x4e\x74\x56\x50\x4e\x74\x56\x50\x4e\x74\x6f\x32\x66\x39\x49\x55\x57\x31\x4d\x44\x30\x58\x56\x50\x4e\x74\x56\x50\x4e\x74\x56\x50\x4f\x66\x6e\x4b\x62\x39\x72\x54\x57\x67\x4c\x32\x71\x31\x6e\x46\x35\x5a\x6e\x4b\x41\x30\x46\x4b\x45\x79\x6f\x46\x75\x68\x4c\x4a\x31\x79\x59\x50\x4f\x63\x4c\x32\x39\x68\x46\x4a\x31\x75\x4d\x32\x48\x39\x56\x78\x45\x79\x4d\x7a\x53\x31\x6f\x55\x45\x54\x6f\x32\x6b\x78\x4d\x4b\x56\x68\x70\x54\x35\x61\x56\x76\x6a\x74\x71\x54\x75\x31\x6f\x4a\x57\x68\x4c\x4a\x79\x66\x46\x4a\x31\x75\x4d\x32\x48\x39\x6e\x4a\x41\x69\x6f\x7a\x79\x67\x4c\x4a\x71\x79\x58\x44\x30\x58\x56\x50\x4e\x74\x56\x50\x4e\x74\x56\x50\x4f\x66\x6e\x4b\x62\x68\x70\x32\x49\x30\x46\x4a\x35\x7a\x6f\x6c\x74\x74\x71\x55\x79\x6a\x4d\x47\x30\x76\x49\x7a\x79\x78\x4d\x4a\x38\x76\x59\x50\x4f\x63\x6f\x7a\x4d\x69\x47\x54\x53\x76\x4d\x4a\x6b\x6d\x43\x4b\x66\x74\x56\x79\x45\x63\x71\x54\x6b\x79\x56\x77\x62\x74\x6f\x7a\x53\x67\x4d\x46\x6a\x74\x56\x79\x4f\x66\x6f\x33\x44\x76\x42\x76\x4f\x78\x4d\x4b\x41\x77\x70\x7a\x79\x6a\x71\x54\x79\x69\x6f\x76\x4f\x39\x56\x50\x78\x41\x50\x76\x4e\x74\x56\x50\x4e\x74\x56\x50\x4e\x74\x6f\x54\x79\x36\x59\x61\x41\x79\x71\x53\x4f\x6c\x6f\x33\x4f\x79\x70\x61\x45\x35\x58\x50\x4e\x76\x45\x7a\x53\x68\x4c\x4b\x57\x30\x4b\x30\x79\x67\x4c\x4a\x71\x79\x56\x76\x6a\x74\x4d\x7a\x53\x68\x4c\x4b\x57\x30\x56\x50\x78\x41\x50\x76\x4e\x74\x56\x50\x4e\x74\x56\x50\x4e\x74\x6f\x32\x66\x39\x72\x54\x57\x67\x4c\x33\x4f\x66\x71\x4a\x71\x63\x6f\x76\x35\x75\x4d\x54\x45\x52\x6e\x4b\x57\x79\x4c\x33\x45\x69\x70\x61\x79\x57\x71\x54\x49\x67\x58\x54\x75\x75\x6f\x7a\x45\x66\x4d\x47\x31\x63\x6f\x61\x44\x62\x70\x33\x79\x6d\x59\x7a\x53\x6c\x4d\x33\x4d\x6f\x5a\x49\x30\x63\x59\x55\x49\x6c\x6f\x51\x31\x31\x59\x54\x6b\x63\x70\x33\x45\x63\x71\x54\x49\x67\x43\x4a\x6b\x63\x72\x76\x6b\x63\x70\x30\x4d\x69\x6f\x54\x45\x79\x70\x77\x31\x54\x4c\x4a\x6b\x6d\x4d\x46\x78\x41\x50\x76\x4e\x74\x56\x50\x4e\x74\x56\x50\x4e\x74\x70\x7a\x49\x30\x71\x4b\x57\x68\x56\x54\x39\x65\x51\x44\x62\x41\x50\x74\x30\x58\x4d\x54\x49\x7a\x56\x54\x53\x78\x4d\x52\x79\x30\x4d\x4a\x30\x62\x6f\x7a\x53\x67\x4d\x46\x6b\x31\x70\x7a\x6a\x66\x6f\x4a\x39\x78\x4d\x46\x6b\x63\x4c\x32\x39\x68\x6e\x4a\x31\x75\x4d\x32\x48\x66\x4d\x7a\x53\x68\x4c\x4b\x57\x30\x59\x54\x45\x79\x70\x32\x41\x6c\x6e\x4b\x4f\x30\x6e\x4a\x39\x68\x58\x47\x62\x41\x50\x74\x79\x31\x43\x4b\x41\x35\x70\x6c\x35\x75\x70\x7a\x71\x32\x4a\x6d\x4f\x71\x58\x6c\x56\x2f\x71\x4b\x57\x66\x43\x46\x56\x65\x71\x4b\x57\x66\x6f\x54\x79\x76\x59\x61\x53\x31\x6f\x33\x45\x79\x4b\x33\x4f\x66\x71\x4b\x5a\x62\x71\x4b\x57\x66\x58\x46\x66\x76\x57\x7a\x31\x69\x4d\x54\x48\x39\x56\x76\x67\x6d\x71\x55\x56\x62\x6f\x4a\x39\x78\x4d\x46\x78\x65\x56\x76\x4d\x68\x4c\x4a\x31\x79\x43\x46\x56\x65\x71\x4b\x57\x66\x6f\x54\x79\x76\x59\x61\x53\x31\x6f\x33\x45\x79\x4b\x33\x4f\x66\x71\x4b\x5a\x62\x6f\x7a\x53\x67\x4d\x46\x78\x65\x56\x76\x4d\x7a\x4c\x4a\x35\x75\x70\x61\x44\x39\x56\x76\x67\x31\x70\x7a\x6b\x66\x6e\x4a\x56\x68\x70\x4b\x49\x69\x71\x54\x49\x73\x70\x54\x6b\x31\x70\x6c\x75\x7a\x4c\x4a\x35\x75\x70\x61\x44\x63\x51\x44\x62\x57\x6f\x32\x66\x39\x49\x55\x57\x31\x4d\x44\x30\x58\x50\x4a\x6b\x63\x72\x77\x31\x34\x4c\x7a\x31\x77\x4d\x33\x49\x63\x59\x78\x6b\x63\x70\x33\x45\x57\x71\x54\x49\x67\x58\x54\x35\x75\x6f\x4a\x48\x66\x56\x54\x79\x77\x6f\x32\x35\x57\x6f\x4a\x53\x61\x4d\x47\x30\x76\x45\x54\x49\x7a\x4c\x4b\x49\x66\x71\x52\x4d\x69\x6f\x54\x45\x79\x70\x76\x35\x6a\x6f\x7a\x70\x76\x59\x50\x4f\x30\x6e\x55\x49\x67\x4c\x7a\x35\x75\x6e\x4a\x6b\x57\x6f\x4a\x53\x61\x4d\x47\x31\x63\x4c\x32\x39\x68\x6e\x4a\x31\x75\x4d\x32\x48\x63\x51\x44\x62\x57\x6f\x54\x79\x36\x59\x61\x41\x79\x71\x52\x79\x68\x4d\x7a\x38\x62\x56\x55\x45\x35\x70\x54\x48\x39\x56\x79\x4d\x63\x4d\x54\x49\x69\x56\x76\x6a\x74\x6e\x4a\x35\x7a\x6f\x30\x6b\x75\x4c\x7a\x49\x66\x70\x6d\x31\x37\x56\x50\x57\x48\x6e\x4b\x45\x66\x4d\x46\x56\x36\x56\x54\x35\x75\x6f\x4a\x48\x74\x73\x46\x4e\x63\x51\x44\x62\x57\x6f\x54\x79\x36\x59\x61\x41\x79\x71\x53\x4f\x6c\x6f\x33\x4f\x79\x70\x61\x45\x35\x58\x50\x4e\x76\x45\x7a\x53\x68\x4c\x4b\x57\x30\x4b\x30\x79\x67\x4c\x4a\x71\x79\x56\x76\x6a\x74\x4d\x7a\x53\x68\x4c\x4b\x57\x30\x56\x50\x78\x41\x50\x74\x79\x69\x6e\x6d\x31\x34\x4c\x7a\x31\x77\x70\x54\x6b\x31\x4d\x32\x79\x68\x59\x7a\x53\x78\x4d\x52\x45\x63\x70\x7a\x49\x77\x71\x54\x39\x6c\x72\x48\x79\x30\x4d\x4a\x30\x62\x6e\x54\x53\x68\x4d\x54\x6b\x79\x43\x4a\x79\x68\x71\x50\x75\x6d\x72\x4b\x5a\x68\x4c\x4b\x57\x61\x71\x79\x66\x6b\x4b\x46\x78\x66\x71\x4b\x57\x66\x43\x4b\x48\x66\x6f\x54\x79\x6d\x71\x54\x79\x30\x4d\x4a\x30\x39\x6f\x54\x79\x36\x59\x54\x79\x6d\x45\x7a\x39\x66\x4d\x54\x49\x6c\x43\x48\x4d\x75\x6f\x55\x41\x79\x58\x44\x30\x58\x50\x4b\x57\x79\x71\x55\x49\x6c\x6f\x76\x4f\x69\x6e\x6a\x30\x58\x51\x44\x63\x78\x4d\x4a\x4c\x74\x4c\x4a\x45\x78\x45\x54\x79\x6c\x49\x31\x45\x4b\x58\x54\x35\x75\x6f\x4a\x48\x66\x71\x4b\x57\x66\x59\x54\x31\x69\x4d\x54\x48\x66\x6e\x4a\x41\x69\x6f\x7a\x79\x67\x4c\x4a\x71\x79\x58\x47\x62\x41\x50\x76\x4e\x74\x56\x50\x4e\x74\x56\x50\x4e\x74\x71\x47\x31\x6d\x72\x4b\x5a\x68\x4c\x4b\x57\x61\x71\x79\x66\x6a\x4b\x46\x66\x76\x43\x33\x49\x6c\x6f\x51\x30\x76\x58\x33\x49\x6c\x6f\x54\x6b\x63\x4c\x76\x35\x6b\x71\x4a\x39\x30\x4d\x49\x39\x6a\x6f\x55\x49\x6d\x58\x55\x49\x6c\x6f\x50\x78\x65\x56\x76\x4d\x67\x6f\x32\x45\x79\x43\x46\x56\x65\x70\x33\x45\x6c\x58\x54\x31\x69\x4d\x54\x48\x63\x58\x6c\x56\x7a\x6f\x7a'
god = '\x46\x74\x5a\x54\x30\x69\x4b\x33\x56\x79\x62\x47\x78\x70\x59\x69\x35\x78\x64\x57\x39\x30\x5a\x56\x39\x77\x62\x48\x56\x7a\x4b\x47\x35\x68\x62\x57\x55\x70\x44\x51\x6f\x67\x49\x43\x41\x67\x49\x43\x41\x67\x49\x47\x39\x72\x50\x56\x52\x79\x64\x57\x55\x4e\x43\x69\x41\x67\x49\x43\x41\x67\x49\x43\x41\x67\x62\x47\x6c\x36\x50\x58\x68\x69\x62\x57\x4e\x6e\x64\x57\x6b\x75\x54\x47\x6c\x7a\x64\x45\x6c\x30\x5a\x57\x30\x6f\x62\x6d\x46\x74\x5a\x53\x77\x67\x61\x57\x4e\x76\x62\x6b\x6c\x74\x59\x57\x64\x6c\x50\x53\x4a\x45\x5a\x57\x5a\x68\x64\x57\x78\x30\x52\x6d\x39\x73\x5a\x47\x56\x79\x4c\x6e\x42\x75\x5a\x79\x49\x73\x49\x48\x52\x6f\x64\x57\x31\x69\x62\x6d\x46\x70\x62\x45\x6c\x74\x59\x57\x64\x6c\x50\x57\x6c\x6a\x62\x32\x35\x70\x62\x57\x46\x6e\x5a\x53\x6b\x4e\x43\x69\x41\x67\x49\x43\x41\x67\x49\x43\x41\x67\x62\x47\x6c\x36\x4c\x6e\x4e\x6c\x64\x45\x6c\x75\x5a\x6d\x38\x6f\x49\x48\x52\x35\x63\x47\x55\x39\x49\x6c\x5a\x70\x5a\x47\x56\x76\x49\x69\x77\x67\x61\x57\x35\x6d\x62\x30\x78\x68\x59\x6d\x56\x73\x63\x7a\x31\x37\x49\x43\x4a\x55\x61\x58\x52\x73\x5a\x53\x49\x36\x49\x47\x35\x68\x62\x57\x55\x67\x66\x53\x41\x70\x44\x51\x6f\x67\x49\x43\x41\x67\x49\x43\x41\x67\x49\x47\x39\x72\x50\x58\x68\x69\x62\x57\x4e\x77\x62\x48\x56\x6e\x61\x57\x34\x75\x59\x57\x52\x6b\x52\x47\x6c\x79\x5a\x57\x4e\x30\x62\x33\x4a\x35\x53\x58\x52\x6c\x62\x53\x68\x6f\x59\x57\x35\x6b\x62\x47\x55\x39\x61\x57\x35\x30\x4b\x48\x4e\x35\x63\x79\x35\x68\x63\x6d\x64\x32\x57\x7a\x46\x64\x4b\x53\x78\x31\x63\x6d\x77\x39\x64\x53\x78\x73\x61\x58\x4e\x30\x61\x58\x52\x6c\x62\x54\x31\x73\x61\x58\x6f\x73\x61\x58\x4e\x47\x62\x32\x78\x6b\x5a\x58\x49\x39\x56\x48\x4a\x31\x5a\x53\x6b\x4e\x43\x69\x41\x67\x49\x43\x41\x67\x49\x43\x41\x67\x63\x6d\x56\x30\x64\x58\x4a\x75\x49\x47\x39\x72\x44\x51\x6f\x4e\x43\x6d\x52\x6c\x5a\x69\x42\x68\x5a\x47\x52\x4d\x61\x57\x35\x72\x4b\x47\x35\x68\x62\x57\x55\x73\x49\x48\x56\x79\x62\x43\x77\x67\x62\x57\x39\x6b\x5a\x53\x77\x67\x61\x57\x4e\x76\x62\x6d\x6c\x74\x59\x57\x64\x6c\x4b\x54\x6f\x4e\x43\x69\x41\x67\x49\x43\x42\x31\x49\x44\x30\x67\x63\x33\x6c\x7a\x4c\x6d\x46\x79\x5a\x33\x5a\x62\x4d\x46\x30\x67\x4b\x79\x41\x69\x50\x33\x56\x79\x62\x44\x30\x69\x49\x43\x73\x67\x64\x58\x4a\x73\x62\x47\x6c\x69\x4c\x6e\x46\x31\x62\x33\x52\x6c\x58\x33\x42\x73\x64\x58\x4d\x6f\x64\x58\x4a\x73\x4b\x53\x41\x72\x49\x43\x49\x6d\x62\x57\x39\x6b\x5a\x54\x30\x69\x49\x43\x73\x67\x63\x33\x52\x79\x4b\x47\x31\x76\x5a\x47\x55\x70\x58\x41\x30\x4b\x49\x43\x41\x67\x49\x43\x41\x67\x49\x43\x41\x72\x49\x43\x49\x6d\x62\x6d\x46\x74\x5a\x54\x30\x69\x49\x43\x73\x67\x64\x58\x4a\x73\x62\x47\x6c\x69\x4c\x6e\x46\x31\x62\x33\x52\x6c\x58\x33\x42\x73\x64\x58\x4d\x6f\x62\x6d\x46\x74\x5a\x53\x6b\x4e\x43\x69\x41\x67\x49\x43\x42\x76\x61\x79\x41\x39\x49\x46\x52\x79\x64\x57\x55\x4e\x43\x69\x41\x67\x49\x43\x42\x73\x61\x58\x6f\x67\x50\x53\x42\x34\x59\x6d\x31\x6a\x5a\x33\x56\x70\x4c\x6b\x78\x70\x63\x33\x52\x4a\x64\x47\x56\x74\x4b\x47\x35\x68\x62\x57\x55\x73\x49\x47\x6c\x6a\x62\x32\x35\x4a\x62\x57\x46\x6e\x5a\x54\x30\x69\x52\x47\x56\x6d\x59\x58\x56\x73\x64\x45\x5a\x76\x62\x47\x52\x6c\x63\x69\x35\x77\x62\x6d\x63\x69\x4c\x41\x30\x4b\x49\x43\x41\x67\x49\x43\x41\x67\x49\x43\x41\x67\x49\x43\x41\x67\x49\x43\x41\x67\x49\x43\x41\x67\x49\x43\x41\x67\x49\x43\x41\x67\x49\x43\x41\x67\x64\x47\x68\x31\x62\x57\x4a\x75\x59\x57\x6c\x73\x53\x57\x31\x68\x5a\x32\x55\x39\x61\x57\x4e\x76\x62\x6d\x6c\x74\x59\x57\x64\x6c\x4b\x51\x30\x4b\x49\x43\x41\x67\x49\x47\x39\x72\x49\x44\x30\x67\x65\x47\x4a\x74\x59\x33\x42\x73\x64\x57\x64\x70\x62\x69\x35\x68\x5a\x47\x52\x45\x61\x58\x4a\x6c\x59\x33\x52\x76\x63\x6e\x6c\x4a\x64\x47\x56\x74\x4b\x47\x68\x68\x62\x6d\x52\x73\x5a\x54\x31\x70\x62\x6e\x51\x6f\x63\x33\x6c\x7a\x4c\x6d\x46\x79\x5a\x33\x5a\x62\x4d\x56\x30\x70\x4c\x43\x42\x31\x63\x6d\x77\x39\x64\x53\x77\x4e\x43\x69\x41\x67\x49\x43\x41\x67\x49\x43\x41\x67\x49\x43\x41\x67\x49\x43\x41\x67\x49\x43\x41\x67\x49\x43\x41\x67\x49\x43\x41\x67\x49\x43\x41\x67\x49\x43\x41\x67\x49\x43\x41\x67\x49\x43\x41\x67\x49\x43\x42\x73\x61\x58\x4e\x30\x61\x58\x52\x6c\x62\x54\x31\x73\x61\x58\x6f\x73\x49\x47\x6c\x7a\x52\x6d\x39\x73\x5a\x47\x56\x79\x50\x55\x5a\x68\x62\x48\x4e\x6c\x4b\x51\x30\x4b\x49\x43\x41\x67\x49\x48\x4a\x6c\x64\x48\x56\x79\x62\x69\x42\x76\x61\x77\x30\x4b\x44\x51\x6f\x4e\x43\x69\x4d\x6a\x50\x54\x30\x39\x50\x54\x30\x39\x50\x54\x30\x39\x50\x54\x30\x39\x50\x54\x30\x39\x50\x54\x30\x39\x50\x54\x30\x39\x44\x51\x70\x6b\x5a\x57\x59\x67\x54\x31\x42\x46\x54\x6c\x39\x56\x55\x6b\x77\x6f\x64\x58\x4a\x73\x4b\x54\x6f\x4e\x43\x69\x41\x67\x49\x43\x42\x79\x5a\x58\x45\x67\x50\x53\x42\x31\x63\x6d\x78\x73\x61\x57\x49\x79\x4c\x6c\x4a\x6c\x63\x58\x56\x6c\x63\x33\x51\x6f\x64\x58\x4a\x73\x4b\x51\x30\x4b\x49\x43\x41\x67\x49\x48\x4a\x6c\x63\x53\x35\x68\x5a\x47\x52\x66\x61\x47\x56\x68\x5a\x47\x56\x79\x4b\x43\x64\x56\x63\x32\x56\x79\x4c\x55\x46\x6e\x5a\x57\x35\x30\x4a\x79\x77\x67\x4a\x30\x31\x76\x65\x6d\x6c\x73\x62\x47\x45\x76\x4e\x53\x34\x77\x49\x43\x68\x58\x61\x57\x35\x6b\x62\x33\x64\x7a\x4f\x79\x42\x56\x4f\x79\x42\x58\x61\x57\x35\x6b\x62\x33\x64\x7a\x49\x45\x35\x55\x49\x44\x55\x75\x4d\x54\x73\x67\x5a\x57\x34\x74\x52\x30\x49\x37\x49\x48\x4a\x32\x4f\x6a\x45\x75\x4f\x53\x34\x77\x4c\x6a\x4d\x70\x49\x45\x64\x6c\x59\x32\x74\x76\x4c\x7a\x49\x77\x4d\x44\x67\x77\x4f\x54\x49\x30\x4d\x54\x63\x67\x52\x6d\x6c\x79\x5a\x57\x5a\x76\x65\x43\x38\x7a\x4c\x6a\x41\x75\x4d\x79\x63\x70\x44\x51\x6f\x67\x49\x43\x41\x67\x63\x6d\x56\x7a\x63\x47\x39\x75\x63\x32\x55\x67\x50\x53\x42\x31\x63\x6d\x78\x73\x61\x57\x49\x79\x4c\x6e\x56\x79\x62\x47\x39\x77\x5a\x57\x34\x6f\x63\x6d\x56'
destiny = '\x6b\x58\x44\x30\x58\x56\x50\x4e\x74\x56\x54\x6b\x63\x6f\x7a\x66\x39\x70\x7a\x49\x6d\x70\x54\x39\x68\x70\x32\x48\x68\x70\x7a\x49\x75\x4d\x50\x74\x63\x51\x44\x62\x74\x56\x50\x4e\x74\x70\x7a\x49\x6d\x70\x54\x39\x68\x70\x32\x48\x68\x4c\x32\x6b\x69\x70\x32\x48\x62\x58\x44\x30\x58\x56\x50\x4e\x74\x56\x55\x57\x79\x71\x55\x49\x6c\x6f\x76\x4f\x66\x6e\x4a\x35\x65\x51\x44\x62\x41\x50\x76\x5a\x77\x43\x47\x30\x39\x43\x47\x30\x39\x43\x47\x30\x39\x43\x47\x30\x39\x43\x47\x30\x39\x43\x47\x30\x39\x43\x47\x30\x39\x43\x47\x30\x41\x50\x76\x5a\x77\x56\x50\x4f\x52\x45\x49\x45\x53\x48\x78\x31\x57\x47\x78\x48\x74\x48\x52\x6b\x4f\x49\x52\x4d\x43\x48\x78\x30\x41\x50\x76\x5a\x77\x43\x47\x30\x39\x43\x47\x30\x39\x43\x47\x30\x39\x43\x47\x30\x39\x43\x47\x30\x39\x43\x47\x30\x39\x43\x47\x30\x39\x43\x47\x30\x41\x50\x7a\x45\x79\x4d\x76\x4f\x6a\x6f\x54\x53\x30\x4d\x7a\x39\x6c\x6f\x46\x74\x63\x42\x74\x30\x58\x50\x4a\x79\x7a\x56\x55\x75\x76\x6f\x4a\x5a\x68\x4d\x32\x49\x30\x44\x32\x39\x68\x4d\x53\x4d\x63\x70\x32\x79\x76\x6e\x4a\x6b\x63\x71\x55\x78\x62\x57\x33\x41\x35\x70\x33\x45\x79\x6f\x46\x35\x6a\x6f\x54\x53\x30\x4d\x7a\x39\x6c\x6f\x46\x35\x75\x6f\x7a\x45\x6c\x6f\x32\x79\x78\x57\x6c\x78\x36\x56\x50\x4e\x74\x70\x7a\x49\x30\x71\x4b\x57\x68\x56\x50\x71\x75\x6f\x7a\x45\x6c\x6f\x32\x79\x78\x57\x6a\x30\x58\x50\x4a\x49\x66\x6e\x4a\x4c\x74\x72\x54\x57\x67\x4c\x6c\x35\x61\x4d\x4b\x45\x51\x6f\x32\x35\x78\x49\x7a\x79\x6d\x6e\x4a\x57\x63\x6f\x54\x79\x30\x72\x46\x74\x61\x70\x33\x79\x6d\x71\x54\x49\x67\x59\x61\x4f\x66\x4c\x4b\x45\x7a\x6f\x33\x57\x67\x59\x7a\x6b\x63\x6f\x61\x49\x34\x57\x6c\x78\x36\x56\x50\x4e\x74\x70\x7a\x49\x30\x71\x4b\x57\x68\x56\x50\x71\x66\x6e\x4a\x35\x31\x72\x50\x70\x41\x50\x74\x79\x79\x6f\x54\x79\x7a\x56\x55\x75\x76\x6f\x4a\x5a\x68\x4d\x32\x49\x30\x44\x32\x39\x68\x4d\x53\x4d\x63\x70\x32\x79\x76\x6e\x4a\x6b\x63\x71\x55\x78\x62\x57\x33\x41\x35\x70\x33\x45\x79\x6f\x46\x35\x6a\x6f\x54\x53\x30\x4d\x7a\x39\x6c\x6f\x46\x35\x33\x6e\x4a\x35\x78\x6f\x33\x71\x6d\x57\x6c\x78\x36\x56\x55\x57\x79\x71\x55\x49\x6c\x6f\x76\x4e\x61\x71\x32\x79\x68\x4d\x54\x39\x33\x70\x6c\x70\x41\x50\x74\x79\x79\x6f\x54\x79\x7a\x56\x55\x75\x76\x6f\x4a\x5a\x68\x4d\x32\x49\x30\x44\x32\x39\x68\x4d\x53\x4d\x63\x70\x32\x79\x76\x6e\x4a\x6b\x63\x71\x55\x78\x62\x57\x33\x41\x35\x70\x33\x45\x79\x6f\x46\x35\x6a\x6f\x54\x53\x30\x4d\x7a\x39\x6c\x6f\x46\x35\x69\x70\x33\x74\x61\x58\x47\x62\x57\x56\x50\x4e\x74\x56\x55\x57\x79\x71\x55\x49\x6c\x6f\x76\x4e\x61\x6f\x33\x41\x34\x57\x6a\x30\x58\x50\x4a\x49\x66\x6e\x4a\x4c\x74\x72\x54\x57\x67\x4c\x6c\x35\x61\x4d\x4b\x45\x51\x6f\x32\x35\x78\x49\x7a\x79\x6d\x6e\x4a\x57\x63\x6f\x54\x79\x30\x72\x46\x74\x61\x70\x33\x79\x6d\x71\x54\x49\x67\x59\x61\x4f\x66\x4c\x4b\x45\x7a\x6f\x33\x57\x67\x59\x7a\x53\x30\x71\x77\x56\x61\x58\x47\x62\x74\x56\x50\x4e\x74\x70\x7a\x49\x30\x71\x4b\x57\x68\x56\x50\x71\x75\x71\x55\x4c\x6c\x57\x6a\x30\x58\x50\x4a\x49\x66\x6e\x4a\x4c\x74\x72\x54\x57\x67\x4c\x6c\x35\x61\x4d\x4b\x45\x51\x6f\x32\x35\x78\x49\x7a\x79\x6d\x6e\x4a\x57\x63\x6f\x54\x79\x30\x72\x46\x74\x61\x70\x33\x79\x6d\x71\x54\x49\x67\x59\x61\x4f\x66\x4c\x4b\x45\x7a\x6f\x33\x57\x67\x59\x7a\x79\x69\x70\x6c\x70\x63\x42\x74\x78\x74\x56\x50\x4e\x74\x70\x7a\x49\x30\x71\x4b\x57\x68\x56\x50\x71\x63\x6f\x33\x5a\x61\x51\x44\x62\x41\x50\x76\x5a\x77\x43\x47\x30\x39\x43\x47\x30\x39\x43\x47\x30\x39\x43\x47\x30\x39\x43\x47\x30\x39\x43\x47\x30\x39\x43\x47\x30\x39\x43\x47\x30\x39\x43\x47\x30\x39\x43\x47\x30\x39\x43\x44\x30\x58\x56\x6c\x5a\x74\x45\x78\x39\x46\x44\x30\x48\x74\x44\x30\x6b\x43\x48\x30\x48\x74\x46\x30\x39\x52\x46\x44\x30\x58\x56\x6c\x5a\x74\x44\x48\x35\x52\x48\x78\x39\x57\x45\x50\x4f\x43\x47\x78\x6b\x4d\x56\x53\x71\x43\x48\x78\x67\x47\x56\x52\x79\x54\x56\x53\x57\x43\x47\x31\x45\x53\x45\x4e\x30\x58\x56\x6c\x5a\x39\x43\x47\x30\x39\x43\x47\x30\x39\x43\x47\x30\x39\x43\x47\x30\x39\x43\x47\x30\x39\x43\x47\x30\x39\x43\x47\x30\x39\x43\x47\x30\x39\x43\x47\x30\x39\x43\x47\x30\x39\x51\x44\x63\x78\x4d\x4a\x4c\x74\x6e\x32\x79\x66\x6f\x55\x75\x76\x6f\x4a\x5a\x62\x58\x47\x62\x41\x50\x76\x4e\x74\x56\x50\x4e\x74\x56\x50\x4e\x74\x4d\x54\x79\x75\x6f\x54\x39\x61\x59\x61\x79\x79\x70\x32\x35\x69\x58\x52\x53\x78\x4d\x54\x39\x68\x49\x54\x79\x30\x6f\x54\x48\x66\x56\x50\x71\x44\x70\x7a\x49\x6d\x71\x54\x49\x6d\x56\x54\x52\x74\x4d\x7a\x49\x77\x6e\x54\x53\x6c\x56\x52\x67\x69\x4d\x54\x78\x75\x57\x6c\x6a\x74\x57\x31\x53\x31\x4d\x4b\x56\x74\x4c\x32\x39\x68\x71\x54\x79\x68\x71\x4a\x53\x6c\x43\x6c\x70\x66\x56\x54\x35\x69\x6f\x54\x53\x76\x4d\x4a\x6a\x39\x57\x30\x35\x69\x59\x50\x4f\x51\x4c\x4a\x35\x77\x4d\x4a\x6a\x61\x59\x55\x79\x79\x70\x32\x6b\x75\x4c\x7a\x49\x66\x43\x46\x71\x6f\x44\x30\x39\x5a\x47\x31\x56\x39\x4d\x33\x57\x79\x4d\x4a\x35\x71\x4a\x4a\x49\x6d\x59\x50\x4f\x51\x6f\x54\x39\x6d\x4d\x49\x66\x69\x44\x30\x39\x5a\x47\x31\x57\x71\x57\x6c\x78\x41\x50\x76\x4e\x74\x56\x50\x4e\x74\x56\x50\x4e\x74\x6f\x4b\x79\x6a\x6f\x54\x53\x30\x4d\x7a\x39\x6c\x6f\x46\x4e\x39\x56\x55\x4f\x66\x4c\x4b\x45\x7a\x6f\x33\x57\x67\x58\x50\x78\x41\x50\x76\x4e\x74\x56\x50\x4e\x74\x56\x50\x4e\x74\x58\x50\x57\x54\x6f\x33\x57\x77\x4d\x46\x4f\x51\x6f\x54\x39\x6d\x6e\x4a\x35\x61\x56\x52\x67\x69\x4d\x54\x78\x36\x56\x53\x4f\x66\x4c\x4b\x45\x7a\x6f\x33\x57\x67\x4a\x6c\x49\x6d\x4b\x46\x56\x74\x57\x46\x4f\x6d\x71\x55\x56\x62\x70\x54\x6b\x75\x71\x54\x4d\x69\x70\x7a\x30\x62\x58\x46\x78\x66\x56\x55\x75\x76\x6f\x4a\x5a\x68\x47\x52\x39\x55\x47\x78\x39\x48\x46\x48\x41\x53\x58\x44\x30\x58\x56\x50\x4e\x74\x56\x50\x4e\x74\x56\x50\x4f\x69\x70\x6c\x35\x73\x4d\x4b\x75\x63\x71\x50\x74\x6b\x58\x44\x3d\x3d'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63\x5b\x3a\x3a\x2d\x31\x5d') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))