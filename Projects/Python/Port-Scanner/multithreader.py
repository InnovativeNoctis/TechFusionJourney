from concurrent.futures import ThreadPoolExecutor, as_completed

def run_threadpool(func, items, max_workers=100, keep_order=True):
   
    workers = min(max_workers, len(items))

    if keep_order:
        with ThreadPoolExecutor(max_workers=workers) as executor:
            return list(executor.map(lambda args: func(*args) if isinstance(args, tuple) else func(args), items))
    else:
        results = []
        with ThreadPoolExecutor(max_workers=workers) as executor:
            futures = [executor.submit(func, *args) if isinstance(args, tuple) else executor.submit(func, args) 
                       for args in items]
            for future in as_completed(futures):
                results.append(future.result())
        return results
