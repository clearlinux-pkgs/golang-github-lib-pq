Name     : golang-github-lib-pq
Version  : 1.0
Release  : 3
URL      : https://github.com/lib/pq/archive/go1.0-cutoff.tar.gz
Source0  : https://github.com/lib/pq/archive/go1.0-cutoff.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : go

%description
This directory contains certificates and private keys for testing some
SSL-related functionality in Travis.  Do NOT use these certificates for
anything other than testing.

%prep
%setup -q -n pq-go1.0-cutoff

%build

%install
%global gopath /usr/lib/golang
%global library_path github.com/lib/pq
rm -rf %{buildroot}
install -d -p %{buildroot}%{gopath}/src/%{library_path}/
for file in $(find . -iname "*.go") ; do
     install -d -p %{buildroot}%{gopath}/src/%{library_path}/$(dirname $file)
     cp -pav $file %{buildroot}%{gopath}/src/%{library_path}/$file
done

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
export GOPATH=%{buildroot}%{gopath}
go test %{library_path} ||: 

%files
%defattr(-,root,root,-)
/usr/lib/golang/src/github.com/lib/pq/bench_test.go
/usr/lib/golang/src/github.com/lib/pq/buf.go
/usr/lib/golang/src/github.com/lib/pq/conn.go
/usr/lib/golang/src/github.com/lib/pq/conn_test.go
/usr/lib/golang/src/github.com/lib/pq/conn_xact_test.go
/usr/lib/golang/src/github.com/lib/pq/copy.go
/usr/lib/golang/src/github.com/lib/pq/copy_test.go
/usr/lib/golang/src/github.com/lib/pq/doc.go
/usr/lib/golang/src/github.com/lib/pq/encode.go
/usr/lib/golang/src/github.com/lib/pq/encode_test.go
/usr/lib/golang/src/github.com/lib/pq/error.go
/usr/lib/golang/src/github.com/lib/pq/hstore/hstore.go
/usr/lib/golang/src/github.com/lib/pq/hstore/hstore_test.go
/usr/lib/golang/src/github.com/lib/pq/listen_example/doc.go
/usr/lib/golang/src/github.com/lib/pq/notify.go
/usr/lib/golang/src/github.com/lib/pq/notify_test.go
/usr/lib/golang/src/github.com/lib/pq/oid/doc.go
/usr/lib/golang/src/github.com/lib/pq/oid/gen.go
/usr/lib/golang/src/github.com/lib/pq/oid/types.go
/usr/lib/golang/src/github.com/lib/pq/ssl_test.go
/usr/lib/golang/src/github.com/lib/pq/url.go
/usr/lib/golang/src/github.com/lib/pq/url_test.go
/usr/lib/golang/src/github.com/lib/pq/user_posix.go
/usr/lib/golang/src/github.com/lib/pq/user_windows.go
