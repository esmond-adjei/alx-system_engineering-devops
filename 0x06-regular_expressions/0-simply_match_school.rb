#!/usr/bin/env ruby

# puts ARGV[0] =~ /School/ ? ARGV[0] : ""
puts ARGV[0].scan(/School/).join
