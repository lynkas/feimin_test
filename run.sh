if [ "$(uname)" == "Darwin" ]; then
  echo "Running in MAC, auto port killer initiated"
	for port in {10000..10020}
	do
		if [[ "$(lsof -i:$port)" != "" ]]; then
			kill `lsof -i:$port |grep Python|awk '{print $2}'`
		fi
	done
	echo "Port 10000 to 10020 has been released!"
	python3 init.py
  python3 main.py --node a &
  python3 main.py --node b &
  python3 main.py --node c &
  python3 main.py --node d &
  python3 main.py --node e &
  python3 main.py --node f &
  python3 main.py --node g &
  python3 main.py --node h &
  python3 main.py --node i &
  python3 main.py --node j &
  python3 main.py --node k &
  python3 main.py --node l &
  echo "在跑了"
  wait
  echo "跑好了"
  python3 check.py
else
	python win_port_cleaner.py
  python init.py
  python main.py --node a &
  python main.py --node b &
  python main.py --node c &
  python main.py --node d &
  python main.py --node e &
  python main.py --node f &
  python main.py --node g &
  python main.py --node h &
  python main.py --node i &
  python main.py --node j &
  python main.py --node k &
  python main.py --node l &
  echo "在跑了"
  wait
  echo "跑好了"
  python check.py
fi
